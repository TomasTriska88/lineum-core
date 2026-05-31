import * as THREE from 'three';

// UI observer threshold only; not a physics parameter.
const ACTIVE_AMPLITUDE_THRESHOLD = 1000;

export class TopographyEngine {
    constructor(container, phiData, trajData) {
        this.container = container;
        this.phiData = phiData;
        this.trajData = trajData;

        this.currentFrameIndex = 0;
        this.frameCount = phiData.metadata.frame_count;
        this.playbackSpeed = 1.0;
        this.frameTimeCounter = 0;
        this.lastTime = performance.now();
        this._isPaused = false;

        this.showSpiral = false; // 🌀 Toggle for Golden Spiral overlay
        this.harmonicData = null;

        // Visual Clarity Pass controls
        this.debugContactView = false;
        this.showNodeIds = false;

        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 10000);

        // Gate preserveDrawingBuffer to avoid performance impact in production
        const usePreserve = (typeof window !== 'undefined' && (import.meta.env.DEV || window.__playwright_test__));
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: !!usePreserve });

        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.container.appendChild(this.renderer.domElement);

        this.camera.position.set(50, 50, 50);
        this.camera.lookAt(0, 0, 0);

        this.initLights();
        this.initGrid();
        this.initHarmonics();

        this.contactGraphGroup = new THREE.Group();
        this.terrainGroup.add(this.contactGraphGroup);

        this.edgeMaterial = new THREE.LineDashedMaterial({
            color: 0xff6600, // Bright diagnostic orange
            dashSize: 0.6,
            gapSize: 0.3,
            transparent: true,
            opacity: 1.0,
            depthTest: false,
            depthWrite: false
        });

        this.updateTopography(); // 🖼️ Initial render for frame 0

        this.onResizeBound = this.onResize.bind(this);
        window.addEventListener('resize', this.onResizeBound);
    }

    get isPaused() {
        return this._isPaused;
    }

    set isPaused(value) {
        if (this._isPaused !== value) {
            this._isPaused = value;
            if (!value) {
                this.lastTime = performance.now(); // Reset time to prevent huge delta jumps
                this.animate();
            } else {
                cancelAnimationFrame(this.requestID);
            }
        }
    }

    initLights() {
        const ambientLight = new THREE.AmbientLight(0x404040, 3);
        this.scene.add(ambientLight);

        this.dirLight = new THREE.DirectionalLight(0x00ffff, 2);
        this.dirLight.position.set(20, 40, 20);
        this.scene.add(this.dirLight);

        this.pointLight = new THREE.PointLight(0xff00ff, 3, 100);
        this.pointLight.position.set(-20, 20, -20);
        this.scene.add(this.pointLight);
    }

    initGrid() {
        const size = 80;
        const segments = 128;
        this.geometry = new THREE.PlaneGeometry(size, size, segments, segments);
        this.geometry.rotateX(-Math.PI / 2);

        // Group to rotate only the terrain, not the lights
        this.terrainGroup = new THREE.Group();
        this.scene.add(this.terrainGroup);

        this.material = new THREE.MeshPhongMaterial({
            color: 0x00ffff,
            wireframe: true,
            side: THREE.DoubleSide,
            transparent: true,
            opacity: 0.2
        });

        this.plane = new THREE.Mesh(this.geometry, this.material);
        this.terrainGroup.add(this.plane);

        // Solid surface with emissive "glow" for depth
        const solidMaterial = new THREE.MeshPhongMaterial({
            color: 0x050505,
            emissive: 0x001111,
            shininess: 100,
            specular: 0x00ffff,
            side: THREE.DoubleSide
        });
        this.solidPlane = new THREE.Mesh(this.geometry, solidMaterial);
        this.terrainGroup.add(this.solidPlane);

        this.initLinony();
    }

    initLinony() {
        this.linony = [];
        const fiberMaterial = new THREE.LineBasicMaterial({ color: 0xffaa00, transparent: true, opacity: 0.8 });

        // Create 3D fibers (lines) that extend from 2D plane into "depth"
        this.trajData.forEach(traj => {
            // Find first valid point to set initial fiber position
            const firstValid = traj.path.find(p => p !== null);
            if (!firstValid) return;

            const x = (firstValid[0] - 64) * 0.5;
            const z = (firstValid[1] - 64) * 0.5;

            const points = [];
            points.push(new THREE.Vector3(x, 50, z)); // Top
            points.push(new THREE.Vector3(x, -50, z)); // Bottom

            const geometry = new THREE.BufferGeometry().setFromPoints(points);
            const line = new THREE.Line(geometry, fiberMaterial);

            // Add a glowing core at the intersection
            const coreGeom = new THREE.SphereGeometry(0.5, 8, 8);
            const coreMat = new THREE.MeshBasicMaterial({ color: 0xffaa00, transparent: true, opacity: 1.0 });
            const core = new THREE.Mesh(coreGeom, coreMat);

            // Add a halo ring for active nodes in contact debug mode
            const haloGeom = new THREE.RingGeometry(0.8, 1.0, 16);
            haloGeom.rotateX(-Math.PI / 2);
            const haloMat = new THREE.MeshBasicMaterial({
                color: 0x00ffff, // Diagnostic cyan halo
                side: THREE.DoubleSide,
                transparent: true,
                opacity: 0.0,
                depthTest: false,
                depthWrite: false
            });
            const halo = new THREE.Mesh(haloGeom, haloMat);

            // Add text label sprite for optional node IDs display
            const canvas = document.createElement('canvas');
            canvas.width = 64;
            canvas.height = 32;
            const ctx = canvas.getContext('2d');
            ctx.fillStyle = '#00ffff';
            ctx.font = 'bold 18px monospace';
            ctx.textAlign = 'center';
            ctx.fillText(`#${traj.id.toString().slice(-4)}`, 32, 20);

            const texture = new THREE.CanvasTexture(canvas);
            const spriteMat = new THREE.SpriteMaterial({
                map: texture,
                transparent: true,
                opacity: 0.0,
                depthTest: false,
                depthWrite: false
            });
            const labelSprite = new THREE.Sprite(spriteMat);
            labelSprite.position.set(0, 1.2, 0); // Position above the core
            labelSprite.scale.set(3, 1.5, 1);

            const group = new THREE.Group();
            group.add(line);
            group.add(core);
            group.add(halo);
            group.add(labelSprite);

            this.terrainGroup.add(group);
            this.linony.push({ group, traj, core, line, halo, labelSprite });
        });
    }

    initHarmonics() {
        this.harmonicsGroup = new THREE.Group();
        this.scene.add(this.harmonicsGroup);

        // Golden Spiral Geometry (Conceptual Ideal)
        const points = [];
        const a = 0.5; // Scale
        const phi = (1 + Math.sqrt(5)) / 2;
        const b = Math.log(phi) / (Math.PI / 2);

        for (let theta = 0; theta < Math.PI * 6; theta += 0.1) {
            const r = a * Math.exp(b * theta);
            const x = r * Math.cos(theta);
            const z = r * Math.sin(theta);
            points.push(new THREE.Vector3(x, 0, z));
        }

        const geometry = new THREE.BufferGeometry().setFromPoints(points);
        const material = new THREE.LineDashedMaterial({
            color: 0xff00ff,
            transparent: true,
            opacity: 0.4,
            dashSize: 1,
            gapSize: 0.5
        });
        this.goldenSpiral = new THREE.Line(geometry, material);
        if (typeof this.goldenSpiral.computeLineDistances === 'function') {
            this.goldenSpiral.computeLineDistances();
        }
        this.goldenSpiral.visible = false;
        this.harmonicsGroup.add(this.goldenSpiral);
    }

    updateTopography() {
        if (!this.phiData) return;

        const frame = this.phiData.frames[this.currentFrameIndex];
        const positions = this.geometry.attributes.position.array;

        // ⚖️ Normalization: subtract mean to stop "flying upwards" 
        // and focus on the spatial variations (the "wells")
        let sum = 0;
        let count = 0;
        for (let y = 0; y < 64; y++) {
            for (let x = 0; x < 64; x++) {
                sum += frame[y][x];
                count++;
            }
        }
        const meanPhi = sum / count;
        // Calculate max absolute relative phi to scale height dynamically
        let maxAbsPhi = 0.0001;
        for (let y = 0; y < 64; y++) {
            for (let x = 0; x < 64; x++) {
                const val = Math.abs(frame[y][x] - meanPhi);
                if (val > maxAbsPhi) maxAbsPhi = val;
            }
        }
        const hScale = -Math.min(0.2, 15.0 / maxAbsPhi); // Prevents mountains from going off-screen in chaotic runs

        // Visual Clarity Pass: Dim grid & hide solid terrain background in debug view
        if (this.plane && this.plane.material) {
            this.plane.material.opacity = this.debugContactView ? 0.02 : 0.2;
        }
        if (this.solidPlane) {
            this.solidPlane.visible = !this.debugContactView;
        }

        const segments = 128;
        for (let i = 0; i < positions.length; i += 3) {
            // Map 128x128 vertex grid to 64x64 audit data
            const vx = (positions[i] / 80 + 0.5) * 63;
            const vz = (positions[i + 2] / 80 + 0.5) * 63;

            const ix = Math.floor(vx);
            const iy = Math.floor(vz);

            if (ix >= 0 && ix < 64 && iy >= 0 && iy < 64) {
                // Use relative Φ (phi - mean)
                const relativePhi = frame[iy][ix] - meanPhi;
                positions[i + 1] = relativePhi * hScale;
            }
        }

        this.geometry.computeVertexNormals();
        if (typeof this.geometry.computeBoundingBox === 'function') {
            this.geometry.computeBoundingBox();
        }
        if (typeof this.geometry.computeBoundingSphere === 'function') {
            this.geometry.computeBoundingSphere();
        }
        this.geometry.attributes.position.needsUpdate = true;

        // Update linons position and visual states
        this.linony.forEach(c => {
            const path = c.traj.path;

            // 👁️ Precise Visibility Gate: only show if we have a valid point for this frame index
            const point = path[this.currentFrameIndex];

            if (!point) {
                c.group.visible = false;
                return;
            }

            c.group.visible = true;

            const x = point[0]; // x is at index 0 in [x, y, amp, step]
            const y = point[1]; // y is at index 1
            const amplitude = point[2];

            const tx = (x - 64) * 0.5;
            const tz = (y - 64) * 0.5;

            c.group.position.set(tx, 0, tz);

            // Core height follows the local Φ-well depth
            const vx = (tx / 80 + 0.5) * 63;
            const vz = (tz / 80 + 0.5) * 63;
            const ix = Math.floor(vx);
            const iy = Math.floor(vz);

            if (ix >= 0 && ix < 64 && iy >= 0 && iy < 64) {
                const relativePhi = frame[iy][ix] - meanPhi;
                c.core.position.y = relativePhi * hScale;
            }

            // Position halo & label sprite at the core height
            if (c.halo) c.halo.position.y = c.core.position.y;
            if (c.labelSprite) c.labelSprite.position.y = c.core.position.y + 1.2;

            // 👻 Ghost state for unborn linony (amplitude-based)
            if (amplitude < ACTIVE_AMPLITUDE_THRESHOLD) {
                c.core.material.opacity = 0.2;
                c.core.scale.set(0.5, 0.5, 0.5);
                c.line.material.opacity = 0.1;
                c.line.visible = !this.debugContactView; // hide fiber in debug view
                if (c.halo) c.halo.material.opacity = 0.0;
                if (c.labelSprite) c.labelSprite.material.opacity = 0.0;
            } else {
                c.core.material.opacity = 1.0;
                c.core.scale.set(1.0, 1.0, 1.0);
                c.line.material.opacity = 0.5;
                c.line.visible = !this.debugContactView; // hide fiber in debug view

                // Active node visibility options in debug view
                if (c.halo) {
                    c.halo.material.opacity = this.debugContactView ? 0.4 : 0.0;
                    c.halo.material.color.setHex(0x00ffff); // Cyan halo by default
                }
                if (c.labelSprite) {
                    c.labelSprite.material.opacity = (this.debugContactView && this.showNodeIds) ? 1.0 : 0.0;
                }
            }
        });

        // 🔗 Draw Diagnostic ContactGraph edges
        // Clear previous lines
        if (this.contactGraphGroup && this.contactGraphGroup.children) {
            while (this.contactGraphGroup.children.length > 0) {
                const child = this.contactGraphGroup.children[0];
                if (child.geometry) child.geometry.dispose();
                // do NOT dispose child.material if it is the shared this.edgeMaterial
                if (typeof this.contactGraphGroup.remove === 'function') {
                    this.contactGraphGroup.remove(child);
                } else {
                    break;
                }
            }
        }

        const activeLinons = [];
        this.linony.forEach(c => {
            const point = c.traj.path[this.currentFrameIndex];
            if (point && point[2] >= ACTIVE_AMPLITUDE_THRESHOLD) {
                const x = point[0];
                const y = point[1];
                const tx = (x - 64) * 0.5;
                const tz = (y - 64) * 0.5;
                // Get the local ground height
                const vx = (tx / 80 + 0.5) * 63;
                const vz = (tz / 80 + 0.5) * 63;
                const ix = Math.floor(vx);
                const iy = Math.floor(vz);
                let ty = 0;
                if (ix >= 0 && ix < 64 && iy >= 0 && iy < 64) {
                    ty = (frame[iy][ix] - meanPhi) * hScale;
                }
                activeLinons.push({
                    id: c.traj.id,
                    pos: new THREE.Vector3(tx, ty, tz),
                    rawX: x,
                    rawY: y,
                    ref: c
                });
            }
        });

        const inContact = new Set();

        for (let i = 0; i < activeLinons.length; i++) {
            for (let j = i + 1; j < activeLinons.length; j++) {
                const l1 = activeLinons[i];
                const l2 = activeLinons[j];
                const dx = l1.rawX - l2.rawX;
                const dy = l1.rawY - l2.rawY;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 12.0) {
                    // Add slight vertical offset (Y + 0.2) to avoid z-fighting with the grid mesh
                    const p1 = l1.pos.clone().add(new THREE.Vector3(0, 0.2, 0));
                    const p2 = l2.pos.clone().add(new THREE.Vector3(0, 0.2, 0));
                    const points = [p1, p2];
                    const geom = new THREE.BufferGeometry().setFromPoints(points);

                    const line = new THREE.Line(geom, this.edgeMaterial);
                    if (typeof line.computeLineDistances === 'function') {
                        line.computeLineDistances();
                    }
                    this.contactGraphGroup.add(line);

                    inContact.add(l1.id);
                    inContact.add(l2.id);
                }
            }
        }

        // Selected contact pair highlight & color styling (Cyan for active, Orange for contact)
        if (this.debugContactView) {
            this.linony.forEach(c => {
                if (c.halo && c.group.visible && c.traj.path[this.currentFrameIndex] && c.traj.path[this.currentFrameIndex][2] >= ACTIVE_AMPLITUDE_THRESHOLD) {
                    if (inContact.has(c.traj.id)) {
                        c.halo.material.color.setHex(0xff6600); // Diagnostic Orange highlight for contacts
                        c.halo.material.opacity = 0.9;
                    } else {
                        c.halo.material.color.setHex(0x00ffff); // Diagnostic Cyan for non-contact active nodes
                        c.halo.material.opacity = 0.4;
                    }
                }
            });
        }
    }

    animate() {
        if (this._isPaused) return;

        this.requestID = requestAnimationFrame(this.animate.bind(this));

        const currentTime = performance.now();
        const deltaTime = (currentTime - this.lastTime) / 1000;
        this.lastTime = currentTime;

        // ⏱️ Proper frame-rate independent playback
        this.frameTimeCounter += deltaTime * this.playbackSpeed * 10; // Base speed: 10 frames per second

        if (this.frameTimeCounter >= 1) {
            const framesToAdvance = Math.floor(this.frameTimeCounter);
            this.currentFrameIndex = (this.currentFrameIndex + framesToAdvance) % this.frameCount;
            this.frameTimeCounter -= framesToAdvance;
            this.updateTopography();

            // 📡 Notify UI of frame change
            if (this.onFrameUpdate) {
                this.onFrameUpdate(this.currentFrameIndex);
            }
        }

        // Animate the edge material dashOffset for a crawling diagnostic pulse effect
        if (this.edgeMaterial) {
            this.edgeMaterial.dashOffset -= 0.02;
        }

        // Pulse active halos in debug mode
        if (this.debugContactView) {
            const time = performance.now() * 0.005;
            const pulse = 1.0 + Math.sin(time) * 0.15;
            this.linony.forEach(c => {
                if (c.halo && c.halo.material.opacity > 0) {
                    c.halo.scale.set(pulse, pulse, pulse);
                }
            });
        }

        this.terrainGroup.rotation.y += 0.001;
        this.renderer.render(this.scene, this.camera);
    }

    jumpToFrame(index) {
        if (index >= 0 && index < this.frameCount) {
            this.currentFrameIndex = index;
            this.frameTimeCounter = 0;
            this.updateTopography();
            if (this.onFrameUpdate) {
                this.onFrameUpdate(this.currentFrameIndex);
            }
            this.renderer.render(this.scene, this.camera);
        }
    }

    focusOnActiveContacts() {
        const activeLinons = [];
        this.linony.forEach(c => {
            const point = c.traj.path[this.currentFrameIndex];
            if (point && point[2] >= ACTIVE_AMPLITUDE_THRESHOLD) {
                const tx = (point[0] - 64) * 0.5;
                const tz = (point[1] - 64) * 0.5;
                const ty = c.core ? c.core.position.y : 0;
                activeLinons.push(new THREE.Vector3(tx, ty, tz));
            }
        });

        const contactPoints = [];
        for (let i = 0; i < this.linony.length; i++) {
            for (let j = i + 1; j < this.linony.length; j++) {
                const c1 = this.linony[i];
                const c2 = this.linony[j];
                const p1 = c1.traj.path[this.currentFrameIndex];
                const p2 = c2.traj.path[this.currentFrameIndex];
                if (p1 && p2 && p1[2] >= ACTIVE_AMPLITUDE_THRESHOLD && p2[2] >= ACTIVE_AMPLITUDE_THRESHOLD) {
                    const dx = p1[0] - p2[0];
                    const dy = p1[1] - p2[1];
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    if (dist < 12.0) {
                        const tx1 = (p1[0] - 64) * 0.5;
                        const tz1 = (p1[1] - 64) * 0.5;
                        const tx2 = (p2[0] - 64) * 0.5;
                        const tz2 = (p2[1] - 64) * 0.5;
                        const ty1 = c1.core ? c1.core.position.y : 0;
                        const ty2 = c2.core ? c2.core.position.y : 0;
                        contactPoints.push(new THREE.Vector3((tx1 + tx2) * 0.5, (ty1 + ty2) * 0.5, (tz1 + tz2) * 0.5));
                    }
                }
            }
        }

        if (contactPoints.length > 0) {
            // Focus on the first contact pair midpoint to avoid height averaging issues
            const centroid = contactPoints[0];

            // Transform local centroid to world space
            this.terrainGroup.updateMatrixWorld(true);
            const worldCentroid = centroid.clone().applyMatrix4(this.terrainGroup.matrixWorld);

            // Position camera closer to focus on contact pair
            this.camera.position.set(worldCentroid.x + 15, worldCentroid.y + 15, worldCentroid.z + 15);
            this.camera.lookAt(worldCentroid);
        } else if (activeLinons.length > 0) {
            // Focus on the first active linon position
            const centroid = activeLinons[0];

            // Transform local centroid to world space
            this.terrainGroup.updateMatrixWorld(true);
            const worldCentroid = centroid.clone().applyMatrix4(this.terrainGroup.matrixWorld);

            this.camera.position.set(worldCentroid.x + 20, worldCentroid.y + 20, worldCentroid.z + 20);
            this.camera.lookAt(worldCentroid);
        }

        this.renderer.render(this.scene, this.camera);
    }

    onResize() {
        this.camera.aspect = window.innerWidth / window.innerHeight;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(window.innerWidth, window.innerHeight);
    }

    dispose() {
        cancelAnimationFrame(this.requestID);
        window.removeEventListener('resize', this.onResizeBound);

        // Dispose of main grid
        if (this.geometry) this.geometry.dispose();
        if (this.material) this.material.dispose();
        if (this.solidPlane && this.solidPlane.material) this.solidPlane.material.dispose();

        // Dispose of linony fibers, cores, halos, and label sprites
        if (this.linony) {
            this.linony.forEach(c => {
                if (c.line.geometry) c.line.geometry.dispose();
                if (c.line.material) c.line.material.dispose();
                if (c.core.geometry) c.core.geometry.dispose();
                if (c.core.material) c.core.material.dispose();
                if (c.halo) {
                    if (c.halo.geometry) c.halo.geometry.dispose();
                    if (c.halo.material) c.halo.material.dispose();
                }
                if (c.labelSprite) {
                    if (c.labelSprite.material) {
                        if (c.labelSprite.material.map) c.labelSprite.material.map.dispose();
                        c.labelSprite.material.dispose();
                    }
                }
            });
        }

        if (this.edgeMaterial) {
            this.edgeMaterial.dispose();
        }

        // Dispose of harmonics
        if (this.goldenSpiral) {
            if (this.goldenSpiral.geometry) this.goldenSpiral.geometry.dispose();
            if (this.goldenSpiral.material) this.goldenSpiral.material.dispose();
        }

        // Dispose of contact graph lines
        if (this.contactGraphGroup && this.contactGraphGroup.children) {
            while (this.contactGraphGroup.children.length > 0) {
                const child = this.contactGraphGroup.children[0];
                if (child.geometry) child.geometry.dispose();
                // do NOT dispose child.material if it is the shared this.edgeMaterial
                if (typeof this.contactGraphGroup.remove === 'function') {
                    this.contactGraphGroup.remove(child);
                } else {
                    break;
                }
            }
        }

        // Dispose renderer context
        if (this.renderer) {
            this.renderer.dispose();
            this.renderer.forceContextLoss();
            if (this.renderer.domElement && this.renderer.domElement.parentNode) {
                this.renderer.domElement.parentNode.removeChild(this.renderer.domElement);
            }
        }
    }
}
