/**
 * veltest.test.js
 * Unit tests for the veltest micro-assertion framework itself.
 */

import { describe, it, expect, runTests } from './veltest.js';

describe('veltest Matchers Self-Verification', () => {
  it('toBe matches identical values', () => {
    expect(42).toBe(42);
    expect('velum').toBe('velum');
    expect(true).toBe(true);
  });

  it('toBe fails on different values', () => {
    let threw = false;
    try {
      expect(42).toBe(100);
    } catch (err) {
      threw = true;
      expect(err.message).toContain('Expected 100, but got 42');
    }
    expect(threw).toBeTruthy();
  });

  it('toBeTruthy and toBeFalsy validate truthiness', () => {
    expect(true).toBeTruthy();
    expect(1).toBeTruthy();
    expect('non-empty').toBeTruthy();
    
    expect(false).toBeFalsy();
    expect(0).toBeFalsy();
    expect('').toBeFalsy();
  });

  it('toContain searches substrings', () => {
    expect('Velum Programming Language').toContain('Programming');
    
    let threw = false;
    try {
      expect('Velum').toContain('React');
    } catch (err) {
      threw = true;
    }
    expect(threw).toBeTruthy();
  });
});

runTests();
