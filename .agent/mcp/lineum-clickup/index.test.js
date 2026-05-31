import test from 'node:test';
import assert from 'node:assert';
import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

/**
 * Sends a sequence of JSON-RPC messages to a spawned MCP server and
 * collects all responses until a timeout fires.
 */
function runMcpSession(messages, timeoutMs = 6000, extraEnv = {}) {
  return new Promise((resolve, reject) => {
    const cp = spawn('node', ['index.js'], {
      cwd: __dirname,
      env: { ...process.env, CLICKUP_API_KEY: 'test-key', ...extraEnv }
    });

    const responses = [];
    let buffer = '';

    cp.stdout.on('data', (data) => {
      buffer += data.toString();
      const lines = buffer.split('\n');
      buffer = lines.pop(); // keep incomplete last line
      for (const line of lines) {
        if (!line.trim()) continue;
        try { responses.push(JSON.parse(line)); } catch (_) {}
      }
    });

    cp.on('error', reject);

    const timer = setTimeout(() => {
      cp.kill();
      resolve(responses);
    }, timeoutMs);

    cp.on('close', () => {
      clearTimeout(timer);
      resolve(responses);
    });

    // MCP handshake
    cp.stdin.write(JSON.stringify({
      jsonrpc: '2.0', id: 1, method: 'initialize',
      params: { protocolVersion: '2024-11-05', capabilities: {}, clientInfo: { name: 'test', version: '1.0' } }
    }) + '\n');
    cp.stdin.write(JSON.stringify({ jsonrpc: '2.0', id: 2, method: 'initialized', params: {} }) + '\n');

    // Send all test messages
    messages.forEach(m => cp.stdin.write(JSON.stringify(m) + '\n'));

    // Allow processing time then close stdin
    setTimeout(() => cp.stdin.end(), timeoutMs - 800);
  });
}

// ── Boot test ─────────────────────────────────────────────────────────────────

test('MCP server boots and returns unique tools without crashing', async () => {
  return new Promise((resolve, reject) => {
    const cp = spawn('node', ['index.js'], {
      cwd: __dirname,
      env: { ...process.env, CLICKUP_API_KEY: 'test-key' }
    });

    let output = '';

    cp.stdout.on('data', (data) => {
      output += data.toString();

      if (output.includes('"id":2')) {
        const lines = output.trim().split('\n');
        for (const line of lines) {
          try {
            const msg = JSON.parse(line);
            if (msg.id === 2 && msg.result && msg.result.tools) {
              const tools = msg.result.tools;
              const names = tools.map(t => t.name);
              const uniqueNames = new Set(names);

              // This assertion ensures the duplicate-tool bug never returns
              assert.strictEqual(
                names.length,
                uniqueNames.size,
                `Duplicate tools found in MCP server! Tool names: ${names.join(', ')}`
              );

              // Assert that update_task schema correctly exposes DoB Gate metadata
              const updateTask = tools.find(t => t.name === 'update_task');
              assert.ok(updateTask, 'update_task tool not found in server response');
              assert.ok(
                updateTask.inputSchema.properties.dob_audit_confirmed,
                'update_task schema is missing dob_audit_confirmed property'
              );
              assert.ok(
                updateTask.inputSchema.properties.status.description.includes("Setting 'blocked' requires dob_audit_confirmed: true"),
                'update_task status description does not warn about DoB gate requirement'
              );

              // Assert new tools are present
              const createFolderTool = tools.find(t => t.name === 'create_folder');
              assert.ok(createFolderTool, 'create_folder tool not found in server response');
              assert.strictEqual(createFolderTool.inputSchema.required.includes('space_id'), true);
              assert.strictEqual(createFolderTool.inputSchema.required.includes('name'), true);

              const createListTool = tools.find(t => t.name === 'create_list');
              assert.ok(createListTool, 'create_list tool not found in server response');
              assert.strictEqual(createListTool.inputSchema.required.includes('folder_id'), true);
              assert.strictEqual(createListTool.inputSchema.required.includes('name'), true);

              const getSpaceTool = tools.find(t => t.name === 'get_space');
              assert.ok(getSpaceTool, 'get_space tool not found in server response');
              assert.strictEqual(getSpaceTool.inputSchema.required.includes('space_id'), true);

              cp.kill();
              resolve();
              return;
            }
          } catch (_) {}
        }
      }
    });

    cp.on('error', reject);
    cp.on('close', (code) => {
      if (code !== 0 && code !== null) {
        reject(new Error(`MCP server process exited unexpectedly with code ${code}`));
      }
    });

    cp.stdin.write(JSON.stringify({
      jsonrpc: '2.0', id: 1, method: 'initialize',
      params: { protocolVersion: '2024-11-05', capabilities: {}, clientInfo: { name: 'test-client', version: '1.0.0' } }
    }) + '\n');
    cp.stdin.write(JSON.stringify({ jsonrpc: '2.0', id: 2, method: 'tools/list', params: {} }) + '\n');

    setTimeout(() => {
      cp.kill();
      reject(new Error('Test timed out waiting for MCP server response'));
    }, 3000);
  });
});

// ── Language Gate tests ──────────────────────────────────────────────
// (Removed as the language gate was decommissioned for MCP server purity)


// ── DoD & DoB Gates ─────────────────────────────────────────────

test('Governance Gates (DoD & DoB): status changes to complete/blocked require audit flags', async () => {
  const cases = [
    {
      label: 'DoD: reject complete without dod_audit_confirmed',
      id: 20,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'complete' },
      expectErrorContains: 'DoD Gate'
    },
    {
      label: 'DoD: reject complete with dod_audit_confirmed but missing dod_comment',
      id: 24,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'complete', dod_audit_confirmed: true },
      expectErrorContains: 'DoD Gate'
    },
    {
      label: 'DoD: accept complete with dod_audit_confirmed and dod_comment',
      id: 21,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'complete', dod_audit_confirmed: true, dod_comment: 'DoD: test complete' },
      expectErrorContains: null
    },
    {
      label: 'DoB: reject blocked without dob_audit_confirmed',
      id: 22,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'blocked' },
      expectErrorContains: 'DoB Gate'
    },
    {
      label: 'DoB: accept blocked with dob_audit_confirmed',
      id: 23,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'blocked', dob_audit_confirmed: true },
      expectErrorContains: null
    }
  ];

  const messages = cases.map(({ id, tool, args }) => ({
    jsonrpc: '2.0', id,
    method: 'tools/call',
    params: { name: tool, arguments: args }
  }));

  const responses = await runMcpSession(messages);
  const byId = Object.fromEntries(responses.map(r => [r.id, r]));

  for (const { label, id, expectErrorContains } of cases) {
    const res = byId[id];
    assert.ok(res, `No response received for: "${label}"`);
    
    // The MCP handler returns validation errors as content with isError: true
    const content = res.result?.content?.[0]?.text ?? '';
    const isError = res.result?.isError === true;

    if (expectErrorContains) {
      assert.ok(isError, `Expected error response for "${label}"`);
      assert.ok(
        content.includes(expectErrorContains),
        `Expected error to contain "${expectErrorContains}" for "${label}", got: "${content}"`
      );
    } else {
      // If no gate is hit, it will try to hit the API (which fails due to fake key),
      // but the error message will be from the API, NOT from our internal gates.
      assert.ok(
        !content.includes('DoD Gate') && !content.includes('DoB Gate'),
        `Request unexpectedly hit a governance gate in "${label}": "${content}"`
      );
    }
  }
});

// ── DoR Gate ──────────────────────────────────────────────────────────

test('DoR Gate: create_task requires at least one assignee', async () => {
  const cases = [
    {
      label: 'DoR: reject create_task with no assignees field',
      id: 30,
      args: { list_id: '123', name: 'Task without assignee', description: 'Missing assignee.', dor_comment: 'DoR: test' },
      expectErrorContains: 'DoR Gate'
    },
    {
      label: 'DoR: reject create_task with empty assignees array',
      id: 31,
      args: { list_id: '123', name: 'Task with empty assignees', description: 'Empty array.', assignees: [], dor_comment: 'DoR: test' },
      expectErrorContains: 'DoR Gate'
    },
    {
      label: 'DoR: reject create_task with missing dor_comment',
      id: 33,
      args: { list_id: '123', name: 'Task missing dor comment', description: 'No DoR comment.', assignees: [36315542] },
      expectErrorContains: 'DoR Gate'
    },
    {
      label: 'DoR: accept create_task with assignee and dor_comment provided (may fail at API, not gate)',
      id: 32,
      args: { list_id: '123', name: 'Task with assignee', description: 'Has assignee.', assignees: [36315542], dor_comment: 'DoR: Assignee justified. Research done. Estimate: 1h. Priority: Normal. Language: English.' },
      expectErrorContains: null
    }
  ];

  const messages = cases.map(({ id, args }) => ({
    jsonrpc: '2.0', id,
    method: 'tools/call',
    params: { name: 'create_task', arguments: args }
  }));

  const responses = await runMcpSession(messages);
  const byId = Object.fromEntries(responses.map(r => [r.id, r]));

  for (const { label, id, expectErrorContains } of cases) {
    const res = byId[id];
    assert.ok(res, `No response received for: "${label}"`);

    const content = res.result?.content?.[0]?.text ?? '';
    const isError = res.result?.isError === true;

    if (expectErrorContains) {
      assert.ok(isError, `Expected error response for "${label}"`);
      assert.ok(
        content.includes(expectErrorContains),
        `Expected error to contain "${expectErrorContains}" for "${label}", got: "${content}"`
      );
    } else {
      assert.ok(
        !content.includes('DoR Gate'),
        `Request unexpectedly hit DoR gate in "${label}": "${content}"`
      );
    }
  }
});
// ── SoU Gate ──────────────────────────────────────────────────────────

test('SoU Gate: update_task description change requires sou_comment', async () => {
  const cases = [
    {
      label: 'SoU: reject description update without sou_comment',
      id: 40,
      args: { task_id: 'abc', description: 'Updated description text.' },
      expectErrorContains: 'SoU Gate'
    },
    {
      label: 'SoU: reject description update with empty sou_comment',
      id: 41,
      args: { task_id: 'abc', description: 'Updated description text.', sou_comment: '   ' },
      expectErrorContains: 'SoU Gate'
    },
    {
      label: 'SoU: accept description update with valid sou_comment (may fail at API, not gate)',
      id: 42,
      args: { task_id: 'abc', description: 'Updated description text.', sou_comment: 'Laptop ordered, arrives tomorrow. Paid from personal account as director loan.' },
      expectErrorContains: null
    },
    {
      label: 'SoU: non-description update (status only) does not require sou_comment',
      id: 43,
      args: { task_id: 'abc', status: 'in progress' },
      expectErrorContains: null
    }
  ];

  const messages = cases.map(({ id, args }) => ({
    jsonrpc: '2.0', id,
    method: 'tools/call',
    params: { name: 'update_task', arguments: args }
  }));

  const responses = await runMcpSession(messages);
  const byId = Object.fromEntries(responses.map(r => [r.id, r]));

  for (const { label, id, expectErrorContains } of cases) {
    const res = byId[id];
    assert.ok(res, `No response received for: "${label}"`);

    const content = res.result?.content?.[0]?.text ?? '';
    const isError = res.result?.isError === true;

    if (expectErrorContains) {
      assert.ok(isError, `Expected error response for "${label}"`);
      assert.ok(
        content.includes(expectErrorContains),
        `Expected error to contain "${expectErrorContains}" for "${label}", got: "${content}"`
      );
    } else {
      assert.ok(
        !content.includes('SoU Gate'),
        `Request unexpectedly hit SoU gate in "${label}": "${content}"`
      );
    }
  }
});

// ── SoU on To Do Tasks Gate tests ───────────────────────────

test('SoU on To Do Tasks Gate: prevents SoU comments and requires status transition or Plan prefix for description updates on to do tasks', async () => {
  const cases = [
    {
      label: 'To Do task: reject description update WITHOUT sou_comment',
      id: 60,
      tool: 'update_task',
      args: { task_id: 'abc', description: 'Just planning stuff.' },
      expectErrorContains: 'Plan Gate'
    },
    {
      label: 'To Do task: allow description update WITH sou_comment (which gets auto-prefixed with Plan)',
      id: 61,
      tool: 'update_task',
      args: { task_id: 'abc', description: 'Just planning stuff.', sou_comment: 'Adding requirements for the new laptop' },
      expectErrorContains: null
    },
    {
      label: 'To Do task: allow description update WITH sou_comment when status transitions to in progress',
      id: 62,
      tool: 'update_task',
      args: { task_id: 'abc', description: 'Starting task work.', status: 'in progress', sou_comment: 'Activating task' },
      expectErrorContains: null
    },
    {
      label: 'To Do task: reject add_comment starting with 📝 SoU:',
      id: 63,
      tool: 'add_comment',
      args: { task_id: 'abc', comment_text: '📝 SoU: Reporting progress' },
      expectErrorContains: 'SoU Gate'
    },
    {
      label: 'To Do task: allow add_comment starting with 🛫 DoR:',
      id: 64,
      tool: 'add_comment',
      args: { task_id: 'abc', comment_text: '🛫 DoR: Pre-flight audit' },
      expectErrorContains: null
    },
    {
      label: 'To Do task: allow add_comment starting with 📝 Plan:',
      id: 65,
      tool: 'add_comment',
      args: { task_id: 'abc', comment_text: '📝 Plan: Adding specification details' },
      expectErrorContains: null
    }
  ];

  const messages = cases.map(({ id, tool, args }) => ({
    jsonrpc: '2.0', id,
    method: 'tools/call',
    params: { name: tool, arguments: args }
  }));

  const responses = await runMcpSession(messages, 6000, { MOCK_CLICKUP_TASK_STATUS: 'to do' });
  const byId = Object.fromEntries(responses.map(r => [r.id, r]));

  for (const { label, id, expectErrorContains } of cases) {
    const res = byId[id];
    assert.ok(res, `No response received for: "${label}"`);

    const content = res.result?.content?.[0]?.text ?? '';
    const isError = res.result?.isError === true;

    if (expectErrorContains) {
      assert.ok(isError, `Expected error response for "${label}"`);
      assert.ok(
        content.includes(expectErrorContains),
        `Expected error to contain "${expectErrorContains}" for "${label}", got: "${content}"`
      );
    } else {
      assert.ok(
        !content.includes('SoU Gate') && !content.includes('Plan Gate'),
        `Request unexpectedly hit SoU/Plan gate in "${label}": "${content}"`
      );
    }
  }
});

// ── Research Gate ──────────────────────────────────────────

test('Research Gate: research tasks require user approval in dod_comment to complete', async () => {
  const cases = [
    {
      label: 'Research: reject complete if task name is research and missing approval',
      id: 70,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'complete', dod_audit_confirmed: true, dod_comment: 'DoD: regular completion' },
      expectErrorContains: 'Research Gate'
    },
    {
      label: 'Research: accept complete if task name is research and includes approval',
      id: 71,
      tool: 'update_task',
      args: { task_id: 'abc', status: 'complete', dod_audit_confirmed: true, dod_comment: 'DoD: test complete. User approved: Yes.' },
      expectErrorContains: null
    }
  ];

  const messages = cases.map(({ id, tool, args }) => ({
    jsonrpc: '2.0', id,
    method: 'tools/call',
    params: { name: tool, arguments: args }
  }));

  const responses = await runMcpSession(messages, 6000, { MOCK_CLICKUP_TASK_NAME: 'Research: clickup access control' });
  const byId = Object.fromEntries(responses.map(r => [r.id, r]));

  for (const { label, id, expectErrorContains } of cases) {
    const res = byId[id];
    assert.ok(res, `No response received for: "${label}"`);

    const content = res.result?.content?.[0]?.text ?? '';
    const isError = res.result?.isError === true;

    if (expectErrorContains) {
      assert.ok(isError, `Expected error response for "${label}"`);
      assert.ok(
        content.includes(expectErrorContains),
        `Expected error to contain "${expectErrorContains}" for "${label}", got: "${content}"`
      );
    } else {
      assert.ok(
        !content.includes('Research Gate'),
        `Request unexpectedly hit Research Gate in "${label}": "${content}"`
      );
    }
  }
});

test('delete_list tool handles delete_list tool call and hits API', async () => {
  const messages = [
    {
      jsonrpc: '2.0',
      id: 80,
      method: 'tools/call',
      params: { name: 'delete_list', arguments: { list_id: 'list-123' } }
    }
  ];

  const responses = await runMcpSession(messages, 6000);
  const res = responses.find(r => r.id === 80);
  assert.ok(res);
  const content = res.result?.content?.[0]?.text ?? '';
  // Since we pass 'test-key' as CLICKUP_API_KEY, the API call will return an error,
  // but it proves the delete_list tool is registered and executing the API call.
  assert.ok(content.includes('ClickUp API Error') || content.includes('Unauthorized') || content.includes('API Error') || res.result?.isError === true);
});


