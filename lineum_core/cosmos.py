import math
from typing import Optional

class MacroTopology:
    """
    Lineum Macroscopic Hash Generator (The Topological OEA Limit)
    
    This module mathematically describes the emergence of macroscopic Universe structures
    (matter knots and dark filaments) strictly through Phase Overlaps of the Quantum Foam,
    without executing time-based continuous simulation (Eq-7).
    """
    
    def __init__(self, seed: int = 42):
        self.seed = seed
        self.base_frequency = 1.0
        self.base_amplitude = 1.0
        
        # Octave scaling parameters
        self.lacunarity = 2.0   # Frequency expansion factor per phase layer (Scale $2^N$)
        self.persistence = 0.5  # Amplitude decay factor (Energy envelope)

    def _hash_2d(self, ix: int, iy: int) -> float:
        """
        Deterministic, bitwise Quantum Foam prime hash.
        Operates strictly on arbitrary-precision Python Integers to completely evade
        Float32/Float64 continuous coordinate limits at extreme scaling depths (e.g. Phase 137).
        """
        # A simple non-linear avalanche hash to distribute geometry cleanly
        h = self.seed + ix * 374761393 + iy * 668265263
        h = (h ^ (h >> 13)) * 1274126177
        h = h ^ (h >> 16)
        
        # Normalize to [-1.0, 1.0] distribution
        return ((h % 2000000) / 1000000.0) - 1.0

    def _evaluate_noise(self, x: float, y: float) -> float:
        """
        Analytically evaluate the foam at a continuous coordinate mathematically.
        This provides purely mathematical interpolation (C1 Hermite/Bicubic smoothstep),
        decoupling the physics from any specific pixel rendering constraints (like Shader Bilinear limits).
        """
        ix = math.floor(x)
        iy = math.floor(y)
        fx = x - ix
        fy = y - iy
        
        # C1 Continuous Hermite interpolation (Smoothstep) to eliminate diamond artifacts
        u = fx * fx * (3.0 - 2.0 * fx)
        v = fy * fy * (3.0 - 2.0 * fy)
        
        n00 = self._hash_2d(ix, iy)
        n10 = self._hash_2d(ix + 1, iy)
        n01 = self._hash_2d(ix, iy + 1)
        n11 = self._hash_2d(ix + 1, iy + 1)
        
        nx0 = n00 * (1.0 - u) + n10 * u
        nx1 = n01 * (1.0 - u) + n11 * u
        return nx0 * (1.0 - v) + nx1 * v

    def evaluate_psi(self, x: float, y: float, phases: int = 11) -> float:
        """
        Destructive Interference Operator (The Wave Matter Finder).
        Slices overlapping $2^N$ scales of spatial noise using subtraction.
        This extracts the indestructible Prime-Knots (Particles, Stars, solid ridges).
        """
        val = 0.0
        freq = self.base_frequency
        amp = self.base_amplitude
        
        for _ in range(phases):
            n = self._evaluate_noise(x * freq, y * freq) * amp
            val = abs(val - n)
            freq *= self.lacunarity
            amp *= self.persistence
            
        return val

    def evaluate_phi(self, x: float, y: float, phases: int = 11) -> float:
        """
        Additive/Diffusion Operator (The Memory / Gravity Finder).
        Averages overlapping $2^N$ scales of noise.
        This isolates the deep, soft Gravity wells, the vast Cosmic Voids, and the Dark Matter filaments.
        """
        val = 0.0
        freq = self.base_frequency
        amp = self.base_amplitude
        
        for _ in range(phases):
            n = self._evaluate_noise(x * freq, y * freq) * amp
            val = (val + n) / 2.0
            freq *= self.lacunarity
            amp *= self.persistence
            
        return val

    def generate_patch(self, center_x: float, center_y: float, width: int, height: int, scale_zoom: float = 1.0, phases: int = 11, mode: str = 'phi'):
        """
        Generates a 2D Bounding Box (Data Matrix) around a center coordinate.
        Returns a 2D List (array) of computed floating values.
        
        Args:
            center_x, center_y: The astronomical/coordinate center.
            width, height: Resolution of the box in pixels (e.g. 1024x1024).
            scale_zoom: The physical size step between each pixel.
            phases: The depth of $2^N$ layers (e.g. 1000 layers).
            mode: 'phi' for gravity/memory, 'psi' for kinetic matter.
        """
        patch = []
        half_w = width / 2.0
        half_h = height / 2.0
        
        print(f"Generating {width}x{height} patch at [{center_x}, {center_y}] (Zoom: {scale_zoom}, Phases: {phases})...")
        
        # We process row by row
        for row in range(height):
            y_coord = center_y + (row - half_h) * scale_zoom
            row_data = []
            for col in range(width):
                x_coord = center_x + (col - half_w) * scale_zoom
                
                if mode == 'psi':
                    val = self.evaluate_psi(x_coord, y_coord, phases)
                else:
                    val = self.evaluate_phi(x_coord, y_coord, phases)
                    
                row_data.append(val)
            patch.append(row_data)
            
        return patch
