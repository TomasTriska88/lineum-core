/**
 * Velum Compiler
 * Pure ES2022 JavaScript, zero dependencies.
 * Converts semantic-geometric Velum canvas (.velum JSON) into a Svelte component or Vanilla Custom Element.
 */

// Target compilation registry (Strategy Pattern)
export const targetDrivers = {};

/**
 * Registers a new compilation driver.
 * @param {string} name - Name of the target (e.g. 'svelte', 'vanilla').
 * @param {Function} driverFn - Function that compiles Velum object to string.
 */
export function registerTarget(name, driverFn) {
  targetDrivers[name] = driverFn;
}

/**
 * Validates Velum JSON structure against standard specification rules.
 * @param {object} velum - Parsed Velum JSON structure.
 * @returns {string[]} List of validation error messages.
 */
export function validateVelum(velum) {
  const errors = [];

  if (!velum || typeof velum !== 'object') {
    errors.push('Velum must be a JSON object.');
    return errors;
  }

  if (velum.$schema !== undefined) {
    if (typeof velum.$schema !== 'string') {
      errors.push('Property "$schema" must be a string.');
    } else if (
      !velum.$schema.endsWith('velum-schema.json') &&
      velum.$schema !== 'https://lineum.io/schemas/velum-schema.json'
    ) {
      errors.push('Property "$schema" must point to a valid velum-schema.json path or URL.');
    }
  }

  if (typeof velum.velum_version !== 'string' || !velum.velum_version.trim()) {
    errors.push('Missing or invalid property: "velum_version" must be a non-empty string.');
  } else {
    const semverRegex = /^\d+\.\d+\.\d+$/;
    if (!semverRegex.test(velum.velum_version)) {
      errors.push('Property "velum_version" must match semantic versioning format (X.Y.Z).');
    } else {
      const [major] = velum.velum_version.split('.').map(Number);
      if (major !== 1) {
        errors.push(`Incompatible Velum version: compiler supports version 1.x.x, but input file requires version ${velum.velum_version}.`);
      }
    }
  }

  if (typeof velum.name !== 'string' || !velum.name.trim()) {
    errors.push('Missing or invalid property: "name" must be a non-empty string.');
  }

  if (velum.imports !== undefined && !Array.isArray(velum.imports)) {
    errors.push('Property "imports" must be an array of strings.');
  } else if (Array.isArray(velum.imports)) {
    velum.imports.forEach((imp, i) => {
      if (typeof imp !== 'string') errors.push(`imports[${i}] must be a string.`);
    });
  }

  if (velum.helpers !== undefined && !Array.isArray(velum.helpers)) {
    errors.push('Property "helpers" must be an array of strings.');
  } else if (Array.isArray(velum.helpers)) {
    velum.helpers.forEach((hlp, i) => {
      if (typeof hlp !== 'string') errors.push(`helpers[${i}] must be a string.`);
    });
  }

  if (velum.states !== undefined && (typeof velum.states !== 'object' || velum.states === null || Array.isArray(velum.states))) {
    errors.push('Property "states" must be an object.');
  } else if (velum.states) {
    Object.keys(velum.states).forEach(key => {
      const state = velum.states[key];
      if (typeof state !== 'object' || state === null || state.init === undefined) {
        errors.push(`State "states.${key}" must be an object containing an "init" property.`);
      }
    });
  }

  if (!Array.isArray(velum.nodes)) {
    errors.push('Missing or invalid property: "nodes" must be an array.');
  } else {
    velum.nodes.forEach((node, i) => {
      if (typeof node !== 'object' || node === null) {
        errors.push(`nodes[${i}] must be an object.`);
        return;
      }
      if (typeof node.id !== 'string' || !node.id.trim()) {
        errors.push(`nodes[${i}]: id must be a non-empty string.`);
      }
      if (!Array.isArray(node.pos) || node.pos.length !== 2 || typeof node.pos[0] !== 'number' || typeof node.pos[1] !== 'number') {
        errors.push(`nodes[${i}] (${node.id || 'unknown'}): pos must be an array of exactly 2 numbers.`);
      }
      if (typeof node.type !== 'string' || !node.type.trim()) {
        errors.push(`nodes[${i}] (${node.id || 'unknown'}): type must be a non-empty string.`);
      }
    });
  }

  if (velum.paths !== undefined && !Array.isArray(velum.paths)) {
    errors.push('Property "paths" must be an array.');
  } else if (Array.isArray(velum.paths)) {
    velum.paths.forEach((pathItem, i) => {
      if (typeof pathItem !== 'object' || pathItem === null) {
        errors.push(`paths[${i}] must be an object.`);
        return;
      }
      if (typeof pathItem.from !== 'string' || !pathItem.from.trim()) {
        errors.push(`paths[${i}]: from must be a non-empty string.`);
      }
    });
  }

  return errors;
}

/**
 * Geometrically sorts nodes by coordinates: top-to-bottom (y) and left-to-right (x).
 * @param {object[]} nodes - List of Velum node objects.
 * @returns {object[]} Sorted copy of the nodes array.
 */
export function sortNodes(nodes) {
  return [...nodes].sort((a, b) => {
    if (a.pos[1] !== b.pos[1]) return a.pos[1] - b.pos[1];
    return a.pos[0] - b.pos[0];
  });
}

/**
 * Strips basic TypeScript annotations to make helpers pure JS browser-runnable.
 */
function stripTypeScript(code) {
  return code
    .replace(/\s+as\s+const\b/g, '')
    .replace(/\s+as\s+[a-zA-Z0-9_\[\]]+/g, '')
    .replace(/:\s*(?:string|number|boolean|any|unknown|void|object|Record<[^>]+>|string\[\]|number\[\])/g, '')
    .replace(/<[a-zA-Z0-9_,\s]+>/g, '');
}

/**
 * Compiles Velum to Svelte 5 syntax.
 */
export function compileToSvelte(velum) {
  const { name, imports = [], states = {}, helpers = [], nodes = [], paths = [], custom_styles = '' } = velum;

  let scriptContent = `<script lang="ts">\n`;
  
  imports.forEach(imp => {
    scriptContent += `    ${imp}\n`;
  });

  if (imports.length > 0) scriptContent += '\n';

  helpers.forEach(hlp => {
    scriptContent += `    ${hlp}\n`;
  });

  if (helpers.length > 0) scriptContent += '\n';

  Object.keys(states).forEach(key => {
    const val = states[key];
    const initialValue = typeof val.init === 'string' ? `"${val.init}"` : JSON.stringify(val.init);
    scriptContent += `    let ${key} = $state(${initialValue});\n`;
  });

  const uiNodes = sortNodes(nodes.filter(n => n.id.startsWith('ui.')));
  let htmlContent = '';
  
  const toggleNode = uiNodes.find(n => n.id.includes('DropdownToggle') || n.type === 'dropdown_toggle');
  const menuNode = uiNodes.find(n => n.id.includes('MenuContainer') || n.type === 'menu_container');

  if (toggleNode) {
    const clickPath = paths.find(p => p.from === toggleNode.id && p.action === 'click');
    const toggleAction = clickPath ? clickPath.handler : '';
    
    htmlContent += `<div class="dropdown lang-dropdown" role="menu" tabindex="0">\n`;
    htmlContent += `    <button\n`;
    htmlContent += `        class="dropdown-toggle lang-toggle"\n`;
    if (toggleAction) {
      htmlContent += `        onclick={${toggleAction}}\n`;
    }
    htmlContent += `    >\n`;
    htmlContent += `        {${toggleNode.label_binding || `"${toggleNode.label}"`}}\n`;
    htmlContent += `        <svg class="chevron-icon" class:rotated={${toggleNode.rotate_condition || 'false'}} viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">\n`;
    htmlContent += `            <polyline points="6 9 12 15 18 9"></polyline>\n`;
    htmlContent += `        </svg>\n`;
    htmlContent += `    </button>\n`;

    if (menuNode) {
      const openCondition = menuNode.show_condition || 'true';
      const loopData = menuNode.loop_data || '';
      
      htmlContent += `    <div\n`;
      htmlContent += `        class="dropdown-menu"\n`;
      htmlContent += `        class:mobile-open={${openCondition}}\n`;
      htmlContent += `        style="min-width: max-content;"\n`;
      htmlContent += `    >\n`;

      if (loopData) {
        const itemVar = menuNode.loop_item || 'item';
        const itemLinkPath = paths.find(p => p.from === menuNode.id && p.flow === 'resolve_route');
        const hrefBinding = itemLinkPath ? itemLinkPath.href_binding : `"${menuNode.default_href || '#'}"`;
        const actionBinding = itemLinkPath && itemLinkPath.handler ? `onclick={${itemLinkPath.handler}}` : '';
        const noTranslate = menuNode.no_translate || false;

        htmlContent += `        {#each ${loopData} as ${itemVar}}\n`;
        if (noTranslate) {
          htmlContent += `            <svelte:element\n`;
          htmlContent += `                this={"a"}\n`;
          htmlContent += `                data-no-translate\n`;
        } else {
          htmlContent += `            <a\n`;
        }
        htmlContent += `                href={${hrefBinding}}\n`;
        htmlContent += `                hreflang={${itemVar}.code}\n`;
        htmlContent += `                data-sveltekit-reload\n`;
        if (actionBinding) {
          htmlContent += `                ${actionBinding}\n`;
        }
        htmlContent += `                class="lang-btn"\n`;
        htmlContent += `                class:active={${menuNode.active_condition.replace(/\$item/g, itemVar)}}\n`;
        htmlContent += `            >\n`;
        htmlContent += `                {${itemVar}.label} ({${itemVar}.abbr})\n`;
        if (noTranslate) {
          htmlContent += `            </svelte:element>\n`;
        } else {
          htmlContent += `            </a>\n`;
        }
        htmlContent += `        {/each}\n`;
      }
      
      htmlContent += `    </div>\n`;
    }
    
    htmlContent += `</div>\n`;
  }

  let styleContent = '';
  if (custom_styles) {
    styleContent = `\n<style>\n${custom_styles}\n</style>\n`;
  }

  scriptContent += `</script>\n\n`;

  return `${scriptContent}${htmlContent}${styleContent}`;
}

/**
 * Compiles Velum into Vitest unit test suite using Svelte Testing Library.
 */
export function compileToVitest(velum) {
  const { name, imports = [], states = {}, helpers = [], nodes = [], paths = [] } = velum;
  
  const hasPageStore = imports.some(imp => imp.includes('$app/stores'));
  const hasI18n = imports.some(imp => imp.includes('$lib/i18n'));
  const hasParaglide = imports.some(imp => imp.includes('$lib/paraglide'));

  let testCode = `import { render, fireEvent } from '@testing-library/svelte';\n`;
  testCode += `import { describe, it, expect, vi } from 'vitest';\n`;
  testCode += `import ${name} from '$lib/components/${name}.svelte';\n\n`;

  if (hasPageStore) {
    testCode += `vi.mock('$app/stores', () => {\n`;
    testCode += `  return {\n`;
    testCode += `    page: {\n`;
    testCode += `      subscribe(run) {\n`;
    testCode += `        run({\n`;
    testCode += `          url: new URL('http://127.0.0.1/'),\n`;
    testCode += `          params: {}\n`;
    testCode += `        });\n`;
    testCode += `        return () => {};\n`;
    testCode += `      }\n`;
    testCode += `    }\n`;
    testCode += `  };\n`;
    testCode += `});\n\n`;
  }

  if (hasI18n) {
    testCode += `vi.mock('$lib/i18n', () => {\n`;
    testCode += `  return {\n`;
    testCode += `    i18n: {\n`;
    testCode += `      resolveRoute: vi.fn((path, lang) => \`/\${lang}\${path === '/' ? '' : path}\`)\n`;
    testCode += `    },\n`;
    testCode += `    pathnames: {}\n`;
    testCode += `  };\n`;
    testCode += `});\n\n`;
  }

  if (hasParaglide) {
    testCode += `vi.mock('$lib/paraglide/runtime.js', () => {\n`;
    testCode += `  return {\n`;
    testCode += `    languageTag: vi.fn(() => 'en')\n`;
    testCode += `  };\n`;
    testCode += `});\n\n`;
  }

  testCode += `describe('${name} Component (auto-generated from Velum)', () => {\n`;
  testCode += `  it('renders correctly', () => {\n`;
  testCode += `    const { container } = render(${name});\n`;
  testCode += `    expect(container).toBeTruthy();\n`;
  testCode += `  });\n\n`;

  const uiNodes = sortNodes(nodes.filter(n => n.id.startsWith('ui.')));
  const toggleNode = uiNodes.find(n => n.id.includes('DropdownToggle') || n.type === 'dropdown_toggle');
  const menuNode = uiNodes.find(n => n.id.includes('MenuContainer') || n.type === 'menu_container');

  if (toggleNode) {
    testCode += `  it('renders the dropdown toggle button', () => {\n`;
    testCode += `    const { getByRole } = render(${name});\n`;
    testCode += `    const button = getByRole('button');\n`;
    testCode += `    expect(button).toBeTruthy();\n`;
    if (toggleNode.label) {
      testCode += `    expect(button.textContent?.trim()).toBeTruthy();\n`;
    }
    testCode += `  });\n\n`;

    if (menuNode) {
      testCode += `  it('toggles menu visibility when clicked', async () => {\n`;
      testCode += `    const { getByRole, container } = render(${name});\n`;
      testCode += `    const button = getByRole('button');\n`;
      testCode += `    \n`;
      testCode += `    let menu = container.querySelector('.dropdown-menu');\n`;
      testCode += `    expect(menu?.classList.contains('mobile-open')).toBe(false);\n\n`;
      testCode += `    await fireEvent.click(button);\n`;
      testCode += `    expect(menu?.classList.contains('mobile-open')).toBe(true);\n\n`;
      testCode += `    await fireEvent.click(button);\n`;
      testCode += `    expect(menu?.classList.contains('mobile-open')).toBe(false);\n`;
      testCode += `  });\n\n`;

      if (menuNode.loop_data) {
        testCode += `  it('renders all loop list options', async () => {\n`;
        testCode += `    const { getByRole, container } = render(${name});\n`;
        testCode += `    const button = getByRole('button');\n`;
        testCode += `    await fireEvent.click(button);\n\n`;
        testCode += `    const items = container.querySelectorAll('.lang-btn');\n`;
        testCode += `    expect(items.length).toBeGreaterThan(0);\n`;
        testCode += `  });\n`;
      }
    }
  }

  testCode += `});\n`;
  return testCode;
}

/**
 * Compiles Velum into a zero-dependency vanilla JS unit test (veltest).
 */
export function compileToVeltest(velum, outputPath) {
  const { name, nodes = [] } = velum;
  
  let importPath = `./${name}.js`;
  if (outputPath && (outputPath.includes('tests/components') || outputPath.includes('tests\\components'))) {
    importPath = `../../lib/components/${name}.js`;
  }

  let testCode = `// Node.js DOM mock environment helper\n`;
  testCode += `if (typeof window === 'undefined') {\n`;
  testCode += `  global.window = {};\n`;
  testCode += `  global.document = {\n`;
  testCode += `    createElement() {\n`;
  testCode += `      return {\n`;
  testCode += `        attachShadow() { return { innerHTML: '' }; },\n`;
  testCode += `        setAttribute() {},\n`;
  testCode += `        getAttribute() { return null; },\n`;
  testCode += `        appendChild() {},\n`;
  testCode += `        addEventListener() {},\n`;
  testCode += `        querySelectorAll() { return []; },\n`;
  testCode += `        querySelector() { return null; }\n`;
  testCode += `      };\n`;
  testCode += `    }\n`;
  testCode += `  };\n`;
  testCode += `  global.HTMLElement = class HTMLElement {\n`;
  testCode += `    attachShadow() {\n`;
  testCode += `      this.shadowRoot = {\n`;
  testCode += `        innerHTML: '',\n`;
  testCode += `        querySelector() { return null; },\n`;
  testCode += `        querySelectorAll() { return []; }\n`;
  testCode += `      };\n`;
  testCode += `      return this.shadowRoot;\n`;
  testCode += `    }\n`;
  testCode += `  };\n`;
  testCode += `  global.customElements = {\n`;
  testCode += `    get() { return null; },\n`;
  testCode += `    define() {}\n`;
  testCode += `  };\n`;
  testCode += `}\n\n`;

  testCode += `import { describe, it, expect, runTests } from './veltest.js';\n`;
  testCode += `const { ${name} } = await import('${importPath}');\n\n`;

  testCode += `describe('${name} Component (veltest)', () => {\n`;
  testCode += `  it('can instantiate component', () => {\n`;
  testCode += `    const instance = new ${name}();\n`;
  testCode += `    expect(instance).toBeTruthy();\n`;
  testCode += `  });\n\n`;

  const uiNodes = sortNodes(nodes.filter(n => n.id.startsWith('ui.')));
  const toggleNode = uiNodes.find(n => n.id.includes('DropdownToggle') || n.type === 'dropdown_toggle');

  if (toggleNode) {
    testCode += `  it('has correct initial state values', () => {\n`;
    testCode += `    const instance = new ${name}();\n`;
    if (velum.states) {
      Object.keys(velum.states).forEach(stateKey => {
        const val = velum.states[stateKey];
        const initialValue = typeof val.init === 'string' ? `"${val.init}"` : JSON.stringify(val.init);
        testCode += `    expect(instance.${stateKey}).toBe(${initialValue});\n`;
      });
    }
    testCode += `  });\n`;
  }

  testCode += `});\n\n`;
  testCode += `runTests();\n`;

  return testCode;
}

/**
 * Compiles Velum into pure Vanilla JS Web Component (Custom Element).
 */
export function compileToVanilla(velum) {
  const { name, imports = [], states = {}, helpers = [], nodes = [], paths = [], custom_styles = '' } = velum;

  const tagName = name.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase();
  const processedImports = imports.map(imp => stripTypeScript(imp)).filter(imp => !imp.includes('$app/') && !imp.includes('svelte')).join('\n');

  const helperGetters = [];
  const processedHelpers = [];

  helpers.forEach(hlp => {
    const cleanHlp = stripTypeScript(hlp);
    const derivedMatch = cleanHlp.match(/(?:let|const)\s+(\w+)\s*=\s*\$derived\((.*)\);?/);
    if (derivedMatch) {
      const [_, varName, expression] = derivedMatch;
      helperGetters.push(`  get ${varName}() {\n    return ${expression};\n  }`);
    } else {
      processedHelpers.push(cleanHlp);
    }
  });

  const helpersCode = processedHelpers.join('\n');
  const stateKeys = Object.keys(states);
  
  const uiNodes = sortNodes(nodes.filter(n => n.id.startsWith('ui.')));
  const toggleNode = uiNodes.find(n => n.id.includes('DropdownToggle') || n.type === 'dropdown_toggle');
  const menuNode = uiNodes.find(n => n.id.includes('MenuContainer') || n.type === 'menu_container');

  let htmlTemplate = '';
  let listenerBindings = '';

  if (toggleNode) {
    const clickPath = paths.find(p => p.from === toggleNode.id && p.action === 'click');
    let toggleAction = clickPath ? clickPath.handler : '';
    
    stateKeys.forEach(stateKey => {
      const regex = new RegExp(`\\b${stateKey}\\b`, 'g');
      toggleAction = toggleAction.replace(regex, `this.${stateKey}`);
    });

    let labelBinding = toggleNode.label_binding || `"${toggleNode.label}"`;
    stateKeys.forEach(stateKey => {
      const regex = new RegExp(`\\b${stateKey}\\b`, 'g');
      labelBinding = labelBinding.replace(regex, `this.${stateKey}`);
    });
    helperGetters.forEach(getter => {
      const getterName = getter.match(/get\s+(\w+)/)[1];
      const regex = new RegExp(`\\b${getterName}\\b`, 'g');
      labelBinding = labelBinding.replace(regex, `this.${getterName}`);
    });

    const rotateCondition = toggleNode.rotate_condition || 'false';
    let cleanRotate = rotateCondition;
    stateKeys.forEach(stateKey => {
      const regex = new RegExp(`\\b${stateKey}\\b`, 'g');
      cleanRotate = cleanRotate.replace(regex, `this.${stateKey}`);
    });

    htmlTemplate += `    <div class="dropdown lang-dropdown" role="menu" tabindex="0">\\n`;
    htmlTemplate += `      <button class="dropdown-toggle lang-toggle">\\n`;
    htmlTemplate += `        \${${labelBinding}}\\n`;
    htmlTemplate += `        <svg class="chevron-icon \${${cleanRotate} ? 'rotated' : ''}" viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">\\n`;
    htmlTemplate += `          <polyline points="6 9 12 15 18 9"></polyline>\\n`;
    htmlTemplate += `        </svg>\\n`;
    htmlTemplate += `      </button>\\n`;

    if (toggleAction) {
      listenerBindings += `    const toggleBtn = this.shadowRoot.querySelector('.lang-toggle');\n`;
      listenerBindings += `    if (toggleBtn) {\n`;
      listenerBindings += `      toggleBtn.addEventListener('click', () => {\n`;
      listenerBindings += `        (${toggleAction})();\n`;
      listenerBindings += `      });\n`;
      listenerBindings += `    }\n`;
    }

    if (menuNode) {
      const openCondition = menuNode.show_condition || 'true';
      let cleanOpen = openCondition;
      stateKeys.forEach(stateKey => {
        const regex = new RegExp(`\\b${stateKey}\\b`, 'g');
        cleanOpen = cleanOpen.replace(regex, `this.${stateKey}`);
      });

      const loopData = menuNode.loop_data || '';
      
      htmlTemplate += `      <div class="dropdown-menu \${${cleanOpen} ? 'mobile-open' : ''}" style="min-width: max-content;">\\n`;

      if (loopData) {
        const itemVar = menuNode.loop_item || 'item';
        const itemLinkPath = paths.find(p => p.from === menuNode.id && p.flow === 'resolve_route');
        
        let hrefBinding = itemLinkPath ? itemLinkPath.href_binding : `"${menuNode.default_href || '#'}"`;
        let actionBinding = itemLinkPath && itemLinkPath.handler ? itemLinkPath.handler : '';

        stateKeys.forEach(stateKey => {
          const regex = new RegExp(`\\b${stateKey}\\b`, 'g');
          actionBinding = actionBinding.replace(regex, `this.${stateKey}`);
        });

        let activeCondition = menuNode.active_condition || '';
        stateKeys.forEach(stateKey => {
          const regex = new RegExp(`\\b${stateKey}\\b`, 'g');
          activeCondition = activeCondition.replace(regex, `this.${stateKey}`);
        });
        helperGetters.forEach(getter => {
          const getterName = getter.match(/get\s+(\w+)/)[1];
          const regex = new RegExp(`\\b${getterName}\\b`, 'g');
          activeCondition = activeCondition.replace(regex, `this.${getterName}`);
        });
        activeCondition = activeCondition.replace(/\$item/g, itemVar);

        htmlTemplate += `        \${${loopData}.map(${itemVar} => \`\\n`;
        htmlTemplate += `          <a\\n`;
        htmlTemplate += `            href="\${${hrefBinding}}"\\n`;
        htmlTemplate += `            hreflang="\${${itemVar}.code}"\\n`;
        htmlTemplate += `            data-sveltekit-reload\\n`;
        htmlTemplate += `            class="lang-btn \${${activeCondition} ? 'active' : ''}"\\n`;
        htmlTemplate += `            data-lang-code="\${${itemVar}.code}"\\n`;
        if (menuNode.no_translate) {
          htmlTemplate += `            data-no-translate\\n`;
        }
        htmlTemplate += `          >\\n`;
        htmlTemplate += `            \${${itemVar}.label} (\${${itemVar}.abbr})\\n`;
        htmlTemplate += `          </a>\\n`;
        htmlTemplate += `        \`).join('')}\\n`;

        if (actionBinding) {
          listenerBindings += `    this.shadowRoot.querySelectorAll('.lang-btn').forEach(btn => {\n`;
          listenerBindings += `      btn.addEventListener('click', (e) => {\n`;
          listenerBindings += `        const ${itemVar} = {\n`;
          listenerBindings += `          code: btn.getAttribute('data-lang-code'),\n`;
          listenerBindings += `          label: btn.textContent.trim().split(' ')[0],\n`;
          listenerBindings += `          abbr: btn.textContent.trim().match(/\\((.*)\\)/)?.[1] || ''\n`;
          listenerBindings += `        };\n`;
          listenerBindings += `        (${actionBinding})();\n`;
          listenerBindings += `      });\n`;
          listenerBindings += `    });\n`;
        }
      }
      
      htmlTemplate += `      </div>\\n`;
    }
    
    htmlTemplate += `    </div>\\n`;
  }

  let stateProperties = '';
  stateKeys.forEach(key => {
    stateProperties += `  get ${key}() {\n`;
    stateProperties += `    return this._state.${key};\n`;
    stateProperties += `  }\n\n`;
    stateProperties += `  set ${key}(val) {\n`;
    stateProperties += `    if (this._state.${key} !== val) {\n`;
    stateProperties += `      this._state.${key} = val;\n`;
    stateProperties += `      this.render();\n`;
    stateProperties += `    }\n`;
    stateProperties += `  }\n\n`;
  });

  let classContent = '';
  if (processedImports) {
    classContent += `${processedImports}\n\n`;
  }
  if (helpersCode) {
    classContent += `${helpersCode}\n\n`;
  }
  
  classContent += `export class ${name} extends HTMLElement {\n`;
  classContent += `  constructor() {\n`;
  classContent += `    super();\n`;
  classContent += `    this.attachShadow({ mode: 'open' });\n`;
  classContent += `    this._state = {\n`;
  stateKeys.forEach(key => {
    const val = states[key];
    const initialValue = typeof val.init === 'string' ? `"${val.init}"` : JSON.stringify(val.init);
    classContent += `      ${key}: ${initialValue},\n`;
  });
  classContent += `    };\n`;
  classContent += `  }\n\n`;

  classContent += `  connectedCallback() {\n`;
  classContent += `    this.render();\n`;
  classContent += `  }\n\n`;

  if (helperGetters.length > 0) {
    classContent += helperGetters.join('\n\n') + '\n\n';
  }

  classContent += stateProperties;

  classContent += `  render() {\n`;
  classContent += `    this.shadowRoot.innerHTML = \`\n`;
  if (custom_styles) {
    classContent += `      <style>\n`;
    classContent += `        ${custom_styles}\n`;
    classContent += `      </style>\n`;
  }
  classContent += `${htmlTemplate}`;
  classContent += `    \`;\n`;
  
  if (listenerBindings) {
    classContent += `\n${listenerBindings}`;
  }
  classContent += `  }\n`;
  classContent += `}\n\n`;

  classContent += `if (!customElements.get('${tagName}')) {\n`;
  classContent += `  customElements.define('${tagName}', ${name});\n`;
  classContent += `}\n`;

  return classContent;
}

// Register default target strategies
registerTarget('svelte', compileToSvelte);
registerTarget('vanilla', compileToVanilla);
registerTarget('test-svelte', compileToVitest);
registerTarget('veltest', compileToVeltest);

function printUsage() {
  console.log('Velum Compiler');
  console.log('Usage: node velum-compiler.js <input_file.velum> [output_file.js] [--target <target>]');
}

// ── CLI Main Execution ──────────────────────────────────────────────────
async function main() {
  const fs = await import('fs');
  const path = await import('path');

  const args = process.argv.slice(2);
  if (args.length < 1) {
    printUsage();
    process.exit(1);
  }

  let target = 'vanilla'; // Default to vanilla
  const targetIndex = args.indexOf('--target');
  if (targetIndex !== -1 && args[targetIndex + 1]) {
    target = args[targetIndex + 1];
    args.splice(targetIndex, 2);
  }

  const inputPath = path.resolve(args[0]);
  let outputPath = args[1] ? path.resolve(args[1]) : null;

  if (!fs.existsSync(inputPath)) {
    console.error(`Error: Input file '${inputPath}' does not exist.`);
    process.exit(1);
  }

  try {
    const rawContent = fs.readFileSync(inputPath, 'utf8');
    const velum = JSON.parse(rawContent);

    // CLI parameter --target overrides, fallback to velum.target, fallback to default 'vanilla'
    if (targetIndex === -1 && velum.target) {
      target = velum.target;
    }

    if (!targetDrivers[target]) {
      console.error(`Error: Unsupported target '${target}'. Registered targets: ${Object.keys(targetDrivers).join(', ')}`);
      process.exit(1);
    }

    if (!outputPath) {
      const ext = path.extname(inputPath);
      const dir = path.dirname(inputPath);
      const base = path.basename(inputPath, ext);
      const outExt = target === 'svelte' ? '.svelte' : (target === 'test-svelte' ? '.test.ts' : (target === 'veltest' ? '.veltest.js' : '.js'));
      outputPath = path.join(dir, `${base}${target === 'test-svelte' || target === 'veltest' ? '' : 'Velum'}${outExt}`);
    }

    console.log(`Reading Velum canvas: ${inputPath}...`);
    console.log('Validating Velum structure against standard schema rules...');
    const validationErrors = validateVelum(velum);
    if (validationErrors.length > 0) {
      console.error('❌ Velum validation failed:');
      validationErrors.forEach(err => console.error(`  - ${err}`));
      process.exit(1);
    }

    console.log(`Compiling Velum to '${target}' target: ${outputPath}...`);
    const compiledCode = targetDrivers[target](velum, outputPath);

    fs.writeFileSync(outputPath, compiledCode, 'utf8');
    console.log(`✅ Compilation successful! Generated: ${path.basename(outputPath)}`);
  } catch (err) {
    console.error('❌ Compilation failed:', err.message);
    process.exit(1);
  }
}

// Only execute CLI wrapper if script is run directly
const isDirectRun = typeof process !== 'undefined' && process.argv && process.argv[1] && (
  process.argv[1].endsWith('velum-compiler.js')
);

if (isDirectRun) {
  main().catch(err => {
    console.error(err);
    process.exit(1);
  });
}
