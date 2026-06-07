import { validateVelum, compileToSvelte, sortNodes, compileToVanilla, targetDrivers } from '../velum-compiler.js';

const tests = [];

function test(name, fn) {
  tests.push({ name, fn });
}

const assert = {
  strictEqual(actual, expected, msg) {
    if (actual !== expected) {
      throw new Error(`${msg || 'Assertion failed'}: expected ${JSON.stringify(expected)}, got ${JSON.stringify(actual)}`);
    }
  },
  ok(value, msg) {
    if (!value) {
      throw new Error(msg || 'Assertion failed: value is not truthy');
    }
  }
};

// Mock valid Velum object matching draft-07 schema
const createValidVelum = () => ({
  name: 'TestComponent',
  imports: ['import { onMount } from "svelte";'],
  helpers: ['const limit = 100;'],
  states: {
    isOpen: { init: false }
  },
  nodes: [
    {
      id: 'ui.DropdownToggle',
      pos: [100, 10],
      type: 'dropdown_toggle',
      label: 'Lang',
      rotate_condition: 'isOpen'
    },
    {
      id: 'ui.MenuContainer',
      pos: [100, 60],
      type: 'menu_container',
      show_condition: 'isOpen',
      loop_data: 'langs',
      loop_item: 'lang',
      active_condition: 'lang.code === "en"',
      no_translate: true
    }
  ],
  paths: [
    {
      from: 'ui.DropdownToggle',
      action: 'click',
      handler: '() => { isOpen = !isOpen; }'
    },
    {
      from: 'ui.MenuContainer',
      flow: 'resolve_route',
      href_binding: 'lang.code',
      handler: '() => { isOpen = false; }'
    }
  ],
  custom_styles: '.lang-btn { color: red; }'
});

test('Compiler Velum validation', () => {
  const velum = createValidVelum();
  const errors = validateVelum(velum);
  assert.strictEqual(errors.length, 0, 'Valid Velum should have no errors');
});

test('Compiler rejects missing name', () => {
  const velum = createValidVelum();
  delete velum.name;
  const errors = validateVelum(velum);
  assert.ok(errors.length > 0, 'Should fail without component name');
  assert.ok(errors.some(e => e.includes('name')), 'Error should mention name');
});

test('Compiler rejects invalid node position coordinates', () => {
  const velum = createValidVelum();
  velum.nodes[0].pos = [100]; // Missing Y coordinate
  const errors = validateVelum(velum);
  assert.ok(errors.length > 0, 'Should fail with invalid coordinate array');
  assert.ok(errors.some(e => e.includes('pos')), 'Error should mention pos');
});

test('Compiler rejects malformed states', () => {
  const velum = createValidVelum();
  velum.states = {
    badState: 'not-an-object'
  };
  const errors = validateVelum(velum);
  assert.ok(errors.length > 0, 'Should fail with malformed states dictionary');
  assert.ok(errors.some(e => e.includes('states')), 'Error should mention states');
});

test('Compiler respects no_translate flag in paths and generates svelte:element', () => {
  const velum = createValidVelum();
  const svelteCode = compileToSvelte(velum);
  
  assert.ok(svelteCode.includes('<svelte:element'), 'Should contain svelte:element tag');
  assert.ok(svelteCode.includes('this="a"'), 'Should compile to this="a"');
  assert.ok(svelteCode.includes('data-no-translate'), 'Should contain data-no-translate attribute');
});

test('Compiler visual-geometric sorting sorts top-to-bottom and left-to-right', () => {
  const nodes = [
    { id: 'ui.NodeA', pos: [200, 100], type: 'button' },
    { id: 'ui.NodeB', pos: [100, 20], type: 'button' },
    { id: 'ui.NodeC', pos: [50, 100], type: 'button' },
    { id: 'ui.NodeD', pos: [300, 20], type: 'button' }
  ];

  const sorted = sortNodes(nodes);
  
  assert.strictEqual(sorted[0].id, 'ui.NodeB', 'Should sort NodeB first (smallest y)');
  assert.strictEqual(sorted[1].id, 'ui.NodeD', 'Should sort NodeD second (same y, larger x)');
  assert.strictEqual(sorted[2].id, 'ui.NodeC', 'Should sort NodeC third (larger y, smaller x)');
  assert.strictEqual(sorted[3].id, 'ui.NodeA', 'Should sort NodeA fourth (larger y, larger x)');
});

test('Compiler registers svelte and vanilla drivers', () => {
  assert.ok(targetDrivers.svelte, 'Svelte driver should be registered');
  assert.ok(targetDrivers.vanilla, 'Vanilla driver should be registered');
  assert.strictEqual(targetDrivers.svelte, compileToSvelte, 'Svelte driver should match compileToSvelte');
  assert.strictEqual(targetDrivers.vanilla, compileToVanilla, 'Vanilla driver should match compileToVanilla');
});

test('Compiler vanilla driver output contains Web Component structure', () => {
  const velum = createValidVelum();
  const vanillaCode = compileToVanilla(velum);
  
  assert.ok(vanillaCode.includes('class TestComponent extends HTMLElement'), 'Should declare Custom Element class');
  assert.ok(vanillaCode.includes("customElements.define('test-component', TestComponent)"), 'Should register Custom Element');
  assert.ok(vanillaCode.includes('this.attachShadow({ mode: \'open\' })'), 'Should attach Shadow DOM');
  assert.ok(vanillaCode.includes('get isOpen()'), 'Should define getter for isOpen state');
  assert.ok(vanillaCode.includes('set isOpen(val)'), 'Should define setter for isOpen state');
  assert.ok(vanillaCode.includes('this.render()'), 'Should call render');
});

// Run tests
export function runVelumTests() {
  console.log('--- Running Velum Compiler Pure JS Tests ---');
  let passed = 0;
  let failed = 0;
  
  for (const t of tests) {
    try {
      t.fn();
      console.log(`✔ ${t.name}`);
      passed++;
    } catch (err) {
      console.error(`✖ ${t.name}`);
      console.error(`  Error: ${err.message}`);
      failed++;
    }
  }

  console.log(`\nResults: ${passed} passed, ${failed} failed.`);
  if (failed > 0) {
    if (typeof process !== 'undefined' && process.exit) {
      process.exit(1);
    }
  }
}

// Auto-run if executed from CLI
const isDirectRun = typeof process !== 'undefined' && process.argv && process.argv[1] && (
  process.argv[1].endsWith('velum-compiler.test.js')
);

if (isDirectRun) {
  runVelumTests();
}
