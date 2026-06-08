/**
 * veltest.test.js
 * Unit tests for the veltest micro-assertion framework itself.
 */

import { suite, test, expect, run } from './veltest.js';

// ── Bootstrapping Verification ──────────────────────────────────────────
// To prevent circular reasoning bugs (e.g. if the assertion engine fails
// silently and always returns success), we verify the core matcher logic
// using raw JS conditional assertions before running the suite.
{
  const assert = (condition, msg) => {
    if (!condition) throw new Error(`Bootstrap failed: ${msg}`);
  };

  // Test actual assignment
  const assertion = expect(42);
  assert(assertion.actual === 42, "expect() does not store the actual value.");

  // Test basic toBe success
  try {
    expect(42).toBe(42);
  } catch (err) {
    assert(false, `expect(42).toBe(42) threw error: ${err.message}`);
  }

  // Test basic toBe failure
  let threw = false;
  try {
    expect(42).toBe(100);
  } catch (err) {
    threw = true;
    assert(err.message.includes('Expected 42 to be 100'), `Unexpected failure message: ${err.message}`);
  }
  assert(threw, "expect(42).toBe(100) did not throw an error.");

  // Test basic negation (.not) success
  try {
    expect(42).not.toBe(100);
  } catch (err) {
    assert(false, `expect(42).not.toBe(100) threw error: ${err.message}`);
  }

  // Test basic negation (.not) failure
  threw = false;
  try {
    expect(42).not.toBe(42);
  } catch (err) {
    threw = true;
  }
  assert(threw, "expect(42).not.toBe(42) did not throw an error.");

  console.log("✔ Bootstrap self-verification passed.");
}

// ── Test Suite (Flat Style) ─────────────────────────────────────────────
suite('veltest Matchers Self-Verification');

test('toBe matches identical values', () => {
  expect(42).toBe(42);
  expect('velum').toBe('velum');
  expect(true).toBe(true);
});

test('not.toBe matches different values', () => {
  expect(42).not.toBe(100);
  expect('velum').not.toBe('react');
});

test('toBeTruthy and toBeFalsy validate truthiness', () => {
  expect(true).toBeTruthy();
  expect(1).toBeTruthy();
  expect('non-empty').toBeTruthy();
  
  expect(false).toBeFalsy();
  expect(0).toBeFalsy();
  expect('').toBeFalsy();
});

test('toContain searches substrings', () => {
  expect('Velum Programming Language').toContain('Programming');
  expect('Velum').not.toContain('React');
});

test('lessthan and greaterthan validate boundaries', () => {
  expect(3).should.be.lessthan(5);
  expect(10).should.be.greaterthan(5);
  expect(3).should.not.be.greaterthan(5);
});

test('string validates type', () => {
  expect('hello').should.be.string();
  expect(42).should.not.be.string();
});

test('true and false validate boolean values', () => {
  expect(true).should.be.true();
  expect(false).should.be.false();
  expect(true).should.not.be.false();
});

test('chains multiple assertions with and', () => {
  expect(3).should.be.lessthan(5).and.should.not.be.string();
  test.variable('velum').should.be.string().and.should.contain('lu');
});

run();
