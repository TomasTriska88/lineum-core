import { validateVelum, compileToSvelte, sortNodes, compileToVanilla, compileToVitest, compileToVeltest, targetDrivers } from '../velum-compiler.js';

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
  velum_version: '1.0.0',
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

test('Compiler rejects missing velum_version', () => {
  const velum = createValidVelum();
  delete velum.velum_version;
  const errors = validateVelum(velum);
  assert.ok(errors.length > 0, 'Should fail without velum_version');
  assert.ok(errors.some(e => e.includes('velum_version')), 'Error should mention velum_version');
});

test('Compiler rejects invalid velum_version format', () => {
  const velum = createValidVelum();
  velum.velum_version = '1.0';
  const errors = validateVelum(velum);
  assert.ok(errors.length > 0, 'Should fail with non-semver version');
});

test('Compiler rejects incompatible major version', () => {
  const velum = createValidVelum();
  velum.velum_version = '2.0.0';
  const errors = validateVelum(velum);
  assert.ok(errors.length > 0, 'Should fail with incompatible major version');
  assert.ok(errors.some(e => e.includes('Incompatible Velum version')), 'Error should mention compatibility');
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
  assert.ok(svelteCode.includes('this={"a"}'), 'Should compile to this={"a"}');
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

test('Compiler registers svelte, vanilla, test-svelte and veltest drivers', () => {
  assert.ok(targetDrivers.svelte, 'Svelte driver should be registered');
  assert.ok(targetDrivers.vanilla, 'Vanilla driver should be registered');
  assert.ok(targetDrivers['test-svelte'], 'Test-svelte driver should be registered');
  assert.ok(targetDrivers.veltest, 'Veltest driver should be registered');
  assert.strictEqual(targetDrivers.svelte, compileToSvelte, 'Svelte driver should match compileToSvelte');
  assert.strictEqual(targetDrivers.vanilla, compileToVanilla, 'Vanilla driver should match compileToVanilla');
  assert.strictEqual(targetDrivers['test-svelte'], compileToVitest, 'Test-svelte driver should match compileToVitest');
  assert.strictEqual(targetDrivers.veltest, compileToVeltest, 'Veltest driver should match compileToVeltest');
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

test('Compiler test-svelte driver output contains Vitest testing code', () => {
  const velum = createValidVelum();
  const testCode = compileToVitest(velum);
  
  assert.ok(testCode.includes("import { render, fireEvent } from '@testing-library/svelte'"), 'Should import Svelte Testing Library');
  assert.ok(testCode.includes("import { describe, it, expect, vi } from 'vitest'"), 'Should import Vitest elements');
  assert.ok(testCode.includes("describe('TestComponent Component (auto-generated from Velum)'"), 'Should declare describe block');
  assert.ok(testCode.includes("it('renders correctly'"), 'Should declare renders correctly test');
  assert.ok(testCode.includes("it('renders the dropdown toggle button'"), 'Should declare toggle button rendering test');
  assert.ok(testCode.includes("it('toggles menu visibility when clicked'"), 'Should declare menu visibility toggle test');
});

test('Compiler veltest driver output contains veltest testing code', () => {
  const velum = createValidVelum();
  const testCode = compileToVeltest(velum);
  
  assert.ok(testCode.includes("import { suite, test, expect, run } from './veltest.js';"), 'Should import veltest runner');
  assert.ok(testCode.includes("const { TestComponent } = await import('./TestComponent.js')"), 'Should import Vanilla Custom Element');
  assert.ok(testCode.includes("suite('TestComponent Component (veltest)');"), 'Should declare suite');
  assert.ok(testCode.includes("test('can instantiate component'"), 'Should declare instantiation test');
  assert.ok(testCode.includes("test('has correct initial state values'"), 'Should declare state initialization test');
  assert.ok(testCode.includes("run();"), 'Should run tests');
});

test('Compiler compiles custom tests dynamically if provided', () => {
  const velum = createValidVelum();
  velum.tests = [
    {
      name: 'should click a button',
      steps: [
        { type: 'click', target: '.my-btn' },
        { type: 'assert_class', target: '.panel', class: 'active', exists: true }
      ]
    }
  ];
  
  const testCode = compileToVeltest(velum);
  assert.ok(testCode.includes("test('should click a button'"), 'Should contain custom test name');
  assert.ok(testCode.includes("instance.shadowRoot.querySelector('.my-btn')"), 'Should query custom button');
  assert.ok(testCode.includes("classList.contains('active')"), 'Should check class active');
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
