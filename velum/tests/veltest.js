/**
 * veltest.js
 * Zero-dependency micro BDD/flat assertion library and test runner for Velum.
 */

// ── Node.js DOM Mock Environment ─────────────────────────────────────────
// Automatically mock the DOM if running in a headless/browserless environment
if (typeof window === 'undefined') {
  class MockElement {
    constructor(tagName = 'div') {
      this.tagName = tagName;
      this.listeners = {};
      this.attributes = {};
      this._textContent = '';
      this.classList = {
        classes: new Set(),
        add(c) { this.classes.add(c); },
        remove(c) { this.classes.delete(c); },
        contains(c) { return this.classes.has(c); }
      };
    }
    setAttribute(name, val) { this.attributes[name] = val; }
    getAttribute(name) { return this.attributes[name] || null; }
    addEventListener(event, fn) {
      if (!this.listeners[event]) this.listeners[event] = [];
      this.listeners[event].push(fn);
    }
    click() {
      if (this.listeners['click']) {
        for (const fn of this.listeners['click']) fn();
      }
    }
    get textContent() { return this._textContent; }
    set textContent(val) { this._textContent = val; }
  }

  class MockShadowRoot {
    constructor() {
      this._innerHTML = '';
      this.elements = {};
      this.elementList = [];
    }
    get innerHTML() {
      return this._innerHTML;
    }
    set innerHTML(val) {
      this._innerHTML = val;
      this.elements = {};
      this.elementList = [];

      // Regex to match HTML tags: <tag attributes>textContent
      const tagRegex = /<([a-zA-Z0-9:-]+)([^>]*)>(?:([^<]*))?/g;
      let match;
      while ((match = tagRegex.exec(val)) !== null) {
        const tagName = match[1];
        const attrsRaw = match[2];
        const textContent = match[3] ? match[3].trim() : '';

        if (['style', 'script', 'svg'].includes(tagName)) continue;

        const element = new MockElement(tagName);
        element.textContent = textContent;

        const classMatch = attrsRaw.match(/class=["']([^"']+)["']/);
        if (classMatch) {
          classMatch[1].split(/\s+/).forEach(c => {
            if (c.trim()) element.classList.add(c.trim());
          });
        }

        const idMatch = attrsRaw.match(/id=["']([^"']+)["']/);
        if (idMatch) {
          element.id = idMatch[1];
          element.setAttribute('id', element.id);
        }

        const dataLangMatch = attrsRaw.match(/data-lang-code=["']([^"']+)["']/);
        if (dataLangMatch) {
          element.setAttribute('data-lang-code', dataLangMatch[1]);
        }

        this.elementList.push(element);
      }
    }
    querySelector(selector) {
      if (this.elements[selector]) return this.elements[selector];

      let found = null;
      for (const el of this.elementList) {
        if (selector.startsWith('.')) {
          const className = selector.slice(1);
          if (el.classList.contains(className)) {
            found = el;
            break;
          }
        } else if (selector.startsWith('#')) {
          const idName = selector.slice(1);
          if (el.id === idName) {
            found = el;
            break;
          }
        } else {
          if (el.tagName.toLowerCase() === selector.toLowerCase()) {
            found = el;
            break;
          }
        }
      }

      if (!found) {
        found = new MockElement(selector);
      }

      this.elements[selector] = found;
      return found;
    }
    querySelectorAll(selector) {
      const results = [];
      for (const el of this.elementList) {
        if (selector.startsWith('.')) {
          const className = selector.slice(1);
          if (el.classList.contains(className)) {
            results.push(el);
          }
        } else if (selector.startsWith('#')) {
          const idName = selector.slice(1);
          if (el.id === idName) {
            results.push(el);
          }
        } else {
          if (el.tagName.toLowerCase() === selector.toLowerCase()) {
            results.push(el);
          }
        }
      }
      return results;
    }
  }

  global.window = {};
  global.document = {
    createElement() {
      return new MockElement();
    }
  };
  global.HTMLElement = class HTMLElement {
    attachShadow() {
      this.shadowRoot = new MockShadowRoot();
      return this.shadowRoot;
    }
    connectedCallback() {}
  };
  global.customElements = {
    get() { return null; },
    define() {}
  };
  global.$page = {
    url: new URL('http://127.0.0.1/')
  };
}

// ── Test Runner Core ─────────────────────────────────────────────────────
const tests = [];
let currentSuiteName = '';

/**
 * Sets the current test suite name (flat style).
 */
export function suite(name) {
  currentSuiteName = name;
}

/**
 * Declares a nested test suite block (BDD style).
 */
export function describe(name, fn) {
  const prevSuite = currentSuiteName;
  currentSuiteName = name;
  fn();
  currentSuiteName = prevSuite;
}

/**
 * Declares a test case (BDD/flat style).
 */
export function test(name, fn) {
  tests.push({ suite: currentSuiteName, name, fn });
}

// Attach variable-scoped fluent assertions directly to test function
test.variable = (actual) => new Assertion(actual);

// Alias 'it' to 'test' for Vitest compatibility
export const it = test;

// ── Assertion Matchers ───────────────────────────────────────────────────
class Assertion {
  constructor(actual, isNot = false) {
    this.actual = actual;
    this.isNot = isNot;
  }

  get not() {
    this.isNot = !this.isNot;
    return this;
  }

  get should() {
    return this;
  }

  get be() {
    return this;
  }

  get and() {
    return new Assertion(this.actual);
  }

  _assert(condition, message) {
    const passed = this.isNot ? !condition : condition;
    if (!passed) {
      throw new Error(message);
    }
    return this;
  }

  // Core BDD Matchers
  toBe(expected) {
    return this._assert(
      this.actual === expected,
      `Expected ${JSON.stringify(this.actual)} ${this.isNot ? 'not ' : ''}to be ${JSON.stringify(expected)}`
    );
  }

  toBeTruthy() {
    return this._assert(
      !!this.actual,
      `Expected ${JSON.stringify(this.actual)} ${this.isNot ? 'not ' : ''}to be truthy, but got ${JSON.stringify(this.actual)}`
    );
  }

  toBeFalsy() {
    return this._assert(
      !this.actual,
      `Expected ${JSON.stringify(this.actual)} ${this.isNot ? 'not ' : ''}to be falsy, but got ${JSON.stringify(this.actual)}`
    );
  }

  toContain(substring) {
    return this._assert(
      typeof this.actual === 'string' && this.actual.includes(substring),
      `Expected string "${this.actual}" ${this.isNot ? 'not ' : ''}to contain "${substring}"`
    );
  }

  toBeLessThan(num) {
    return this._assert(
      this.actual < num,
      `Expected ${JSON.stringify(this.actual)} ${this.isNot ? 'not ' : ''}to be less than ${num}`
    );
  }

  toBeGreaterThan(num) {
    return this._assert(
      this.actual > num,
      `Expected ${JSON.stringify(this.actual)} ${this.isNot ? 'not ' : ''}to be greater than ${num}`
    );
  }

  toBeString() {
    return this._assert(
      typeof this.actual === 'string',
      `Expected ${JSON.stringify(this.actual)} ${this.isNot ? 'not ' : ''}to be a string`
    );
  }

  // Fluent Short Aliases
  true() {
    return this.toBe(true);
  }

  false() {
    return this.toBe(false);
  }

  lessthan(num) {
    return this.toBeLessThan(num);
  }

  greaterthan(num) {
    return this.toBeGreaterThan(num);
  }

  string() {
    return this.toBeString();
  }

  contain(substring) {
    return this.toContain(substring);
  }
}

/**
 * Expect assertion helper.
 */
export function expect(actual) {
  return new Assertion(actual);
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
  if (typeof process !== 'undefined' && process.exit) {
    process.exit(failed > 0 ? 1 : 0);
  }
}

// Alias 'run' to 'runTests'
export const run = runTests;
