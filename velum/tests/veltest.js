/**
 * veltest.js
 * Zero-dependency micro BDD assertion library and test runner for Velum.
 */

const tests = [];
let currentSuite = '';

/**
 * Declares a test suite block.
 */
export function describe(name, fn) {
  currentSuite = name;
  fn();
  currentSuite = '';
}

/**
 * Declares an individual test case.
 */
export function it(name, fn) {
  tests.push({ suite: currentSuite, name, fn });
}

/**
 * Expect assertion helper.
 */
export function expect(actual) {
  return {
    toBe(expected) {
      if (actual !== expected) {
        throw new Error(`Expected ${JSON.stringify(expected)}, but got ${JSON.stringify(actual)}`);
      }
    },
    toBeTruthy() {
      if (!actual) {
        throw new Error(`Expected value to be truthy, but got ${JSON.stringify(actual)}`);
      }
    },
    toBeFalsy() {
      if (actual) {
        throw new Error(`Expected value to be falsy, but got ${JSON.stringify(actual)}`);
      }
    },
    toContain(substring) {
      if (typeof actual !== 'string' || !actual.includes(substring)) {
        throw new Error(`Expected string "${actual}" to contain "${substring}"`);
      }
    }
  };
}

/**
 * Runs all registered tests.
 */
export async function runTests() {
  console.log('\n--- Running veltest suite ---');
  let passed = 0;
  let failed = 0;
  
  for (const t of tests) {
    const label = t.suite ? `[${t.suite}] > ${t.name}` : t.name;
    try {
      await t.fn();
      console.log(`✔ ${label}`);
      passed++;
    } catch (err) {
      console.error(`✖ ${label}`);
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
