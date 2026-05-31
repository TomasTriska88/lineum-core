import test from 'node:test';
import assert from 'node:assert';
import { ClickUpAPI, normalizeText } from './api.js';

test('normalizeText unescapes literal \\n and \\t sequences sent by the MCP framework', (t) => {
  assert.strictEqual(normalizeText('line1\\nline2'), 'line1\nline2');
  assert.strictEqual(normalizeText('col1\\tcol2'), 'col1\tcol2');
  assert.strictEqual(normalizeText('no escape sequences'), 'no escape sequences');
  assert.strictEqual(normalizeText(null), null);
  assert.strictEqual(normalizeText(123), 123);
  assert.strictEqual(normalizeText('mixed\\tdata\\nnewline'), 'mixed\tdata\nnewline');
});

// Regression test: dor_comment in create_task was NOT passed through normalizeText(),
// causing literal \\n to be stored in ClickUp comments instead of actual newlines.
// Fix: added `dor_comment = normalizeText(dor_comment)` in index.js create_task handler.
test('normalizeText correctly handles multi-line DoR comment as sent by MCP framework', (t) => {
  const rawFromMcp = '1. Assignee: Tomas Triska\\n\\n2. Research: verified.\\n\\n3. Time estimate: 2h.\\n\\n4. Priority: Urgent.\\n\\n5. Language: English.';
  const expected   = '1. Assignee: Tomas Triska\n\n2. Research: verified.\n\n3. Time estimate: 2h.\n\n4. Priority: Urgent.\n\n5. Language: English.';
  assert.strictEqual(normalizeText(rawFromMcp), expected);
});

test('ClickUpAPI constructor does not throw on missing key, but methods do via requireAuth', async (t) => {
  const api = new ClickUpAPI();
  await assert.rejects(() => api.createTask('123', 'Name'), /CLICKUP_API_KEY environment variable is not configured/);
});


test('createTask throws on missing args', async (t) => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.createTask(), /listId and name are required/);
});

test('createTask sends correct payload', async (t) => {
  const api = new ClickUpAPI('fake-key');
  let callCount = 0;
  
  // Mock fetch — first call is POST to create, second call is PUT to set points
  global.fetch = async (url, options) => {
    callCount++;
    if (callCount === 1) {
      assert.strictEqual(url, 'https://api.clickup.com/api/v2/list/123/task');
      assert.strictEqual(options.method, 'POST');
      assert.strictEqual(options.headers['Authorization'], 'fake-key');
      const body = JSON.parse(options.body);
      assert.strictEqual(body.name, 'Test Task');
      assert.strictEqual(body.priority, 1);
      return { ok: true, json: async () => ({ id: 'mock-id', url: 'mock-url' }) };
    } else {
      // Second call: PUT to set sprint points
      assert.strictEqual(url, 'https://api.clickup.com/api/v2/task/mock-id');
      assert.strictEqual(options.method, 'PUT');
      const body = JSON.parse(options.body);
      assert.strictEqual(body.points, 3);
      return { ok: true, json: async () => ({}) };
    }
  };

  const res = await api.createTask('123', 'Test Task', 'desc', 1, null, false, null, null, 3);
  assert.strictEqual(res.id, 'mock-id');
  assert.strictEqual(callCount, 2); // POST + PUT for points
});

test('createTask handles API errors', async (t) => {
  const api = new ClickUpAPI('fake-key');
  
  global.fetch = async () => ({
    ok: false,
    status: 400,
    text: async () => 'Bad Request'
  });

  await assert.rejects(() => api.createTask('123', 'Test Task'), /ClickUp API Error: 400 - Bad Request/);
});

test('getTasks throws on missing listId', async (t) => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.getTasks(), /listId is required/);
});

test('getTasks fetches list of tasks', async (t) => {
  const api = new ClickUpAPI('fake-key');
  
  global.fetch = async (url, options) => {
    assert.strictEqual(url.includes('order_by'), false);
    assert.strictEqual(options.method, 'GET');
    
    return {
      ok: true,
      json: async () => ({ tasks: [{ id: 'mock-1', priority: { id: "1" } }] })
    };
  };

  const tasks = await api.getTasks('123');
  assert.strictEqual(tasks.length, 1);
  assert.strictEqual(tasks[0].id, 'mock-1');
});

test('updateTaskPriority throws on missing args', async (t) => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.updateTaskPriority(), /taskId and priority are required/);
});

test('updateTaskPriority sends correct payload', async (t) => {
  const api = new ClickUpAPI('fake-key');
  
  global.fetch = async (url, options) => {
    assert.strictEqual(url, 'https://api.clickup.com/api/v2/task/task-123');
    assert.strictEqual(options.method, 'PUT');
    
    const body = JSON.parse(options.body);
    assert.strictEqual(body.priority, 1);
    
    return {
      ok: true,
      json: async () => ({ id: 'task-123' })
    };
  };

  const res = await api.updateTaskPriority('task-123', 1);
  assert.strictEqual(res.id, 'task-123');
});

test('updateTask throws on missing args', async (t) => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.updateTask(), /taskId and updateData are required/);
});

test('updateTask sends correct payload', async (t) => {
  const api = new ClickUpAPI('fake-key');
  
  global.fetch = async (url, options) => {
    assert.strictEqual(url, 'https://api.clickup.com/api/v2/task/task-123');
    assert.strictEqual(options.method, 'PUT');
    
    const body = JSON.parse(options.body);
    assert.strictEqual(body.markdown_description, 'New Context');
    assert.strictEqual(body.description, undefined);
    
    return {
      ok: true,
      json: async () => ({ id: 'task-123' })
    };
  };

  const res = await api.updateTask('task-123', { description: 'New Context' });
  assert.strictEqual(res.id, 'task-123');
});

// Regression test: due_date must be sent as a Unix timestamp in ms, not as an ISO string.
// ISO date strings (e.g. '2026-07-13') must be converted to Unix ms before the API call.
test('updateTask converts ISO due_date string to Unix timestamp in milliseconds', async (t) => {
  const api = new ClickUpAPI('fake-key');

  global.fetch = async (url, options) => {
    const body = JSON.parse(options.body);
    // '2026-07-13T00:00:00.000Z' in Unix ms
    const expectedMs = new Date('2026-07-13T00:00:00.000Z').getTime();
    assert.strictEqual(typeof body.due_date, 'number', 'due_date must be a number (Unix ms), not a string');
    assert.strictEqual(body.due_date, expectedMs, `Expected ${expectedMs}, got ${body.due_date}`);
    return { ok: true, json: async () => ({ id: 'task-123' }) };
  };

  await api.updateTask('task-123', { due_date: '2026-07-13' });
});

test('getWorkspaceHierarchy uses hardcoded WORKSPACE_TEAM_ID in API call', async () => {
  const api = new ClickUpAPI('fake_key');
  let capturedUrl = null;

  global.fetch = async (url) => {
    if (!capturedUrl) capturedUrl = url;
    if (url.includes('/space?')) return { ok: true, json: async () => ({ spaces: [] }) };
    return { ok: true, json: async () => ({}) };
  };

  await api.getWorkspaceHierarchy();
  assert.ok(capturedUrl.includes('90121717552'), `Expected WORKSPACE_TEAM_ID in URL, got: ${capturedUrl}`);
});

test('getSpace and updateSpace throw on missing args', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.getSpace(), /spaceId is required/);
  await assert.rejects(() => api.updateSpace('123'), /spaceId and updateData are required/);
});

test('updateSpace sends correct PUT request with private parameter', async () => {
  const api = new ClickUpAPI('fake_key');
  let capturedUrl = null;
  let capturedBody = null;

  global.fetch = async (url, options) => {
    if (url.includes('/space/123')) {
      const method = options && options.method ? options.method.toUpperCase() : 'GET';
      if (method === 'GET') {
        return { ok: true, json: async () => ({ id: '123', name: 'Test Space' }) };
      }
      if (method === 'PUT') {
        capturedUrl = url;
        capturedBody = JSON.parse(options.body);
        return { ok: true, json: async () => ({ id: '123' }) };
      }
    }
    return { ok: false, text: async () => 'Mock Error' };
  };

  const res = await api.updateSpace('123', { private: true, members: [36315542, 81848905] });
  assert.strictEqual(res.id, '123');
  assert.strictEqual(capturedUrl, 'https://api.clickup.com/api/v2/space/123');
  assert.strictEqual(capturedBody.private, true);
  assert.strictEqual(capturedBody.name, 'Test Space'); // preserved by safety guard
  assert.deepStrictEqual(capturedBody.members, [36315542, 81848905]);
});

test('addComment throws on missing args', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.addComment(), /taskId and commentText required/);
});

test('getWorkspaceUsers uses hardcoded WORKSPACE_TEAM_ID to filter teams', async () => {
  const api = new ClickUpAPI('fake_key');

  global.fetch = async (url, options) => {
    assert.strictEqual(url, 'https://api.clickup.com/api/v2/team');
    return {
      ok: true,
      json: async () => ({
        teams: [
          { id: 'other_team', members: [] },
          { id: '90121717552', members: [{ user: { id: 101, username: 'testuser' } }] }
        ]
      })
    };
  };

  const users = await api.getWorkspaceUsers();
  assert.strictEqual(users.length, 1);
  assert.strictEqual(users[0].id, 101);
});

test('getTask throws on missing taskId', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.getTask(), /taskId is required/);
});

test('getTask fetches full task details including subtasks', async () => {
  const api = new ClickUpAPI('fake_key');

  global.fetch = async (url, options) => {
    assert.ok(url.includes('/task/abc123'));
    assert.ok(url.includes('include_subtasks=true'));
    return {
      ok: true,
      json: async () => ({
        id: 'abc123',
        name: 'Test Task',
        checklists: [{ name: 'QA', items: [{ name: 'Verify access' }] }],
        subtasks: [],
        time_estimate: 7200000
      })
    };
  };

  const task = await api.getTask('abc123');
  assert.strictEqual(task.id, 'abc123');
  assert.strictEqual(task.checklists.length, 1);
});

test('getTaskComments throws on missing taskId', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.getTaskComments(), /taskId is required/);
});

test('getTaskComments fetches comments array', async () => {
  const api = new ClickUpAPI('fake_key');

  global.fetch = async (url, options) => {
    assert.ok(url.includes('/task/abc123/comment'));
    return {
      ok: true,
      json: async () => ({
        comments: [
          { id: 'c1', comment_text: 'First comment' },
          { id: 'c2', comment_text: 'Second comment' }
        ]
      })
    };
  };

  const comments = await api.getTaskComments('abc123');
  assert.strictEqual(comments.length, 2);
  assert.strictEqual(comments[0].comment_text, 'First comment');
});

test('removeDependency throws on missing args', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.removeDependency(), /taskId and dependsOnTaskId required/);
});

test('removeDependency sends correct DELETE request', async () => {
  const api = new ClickUpAPI('fake_key');

  global.fetch = async (url, options) => {
    assert.strictEqual(url, 'https://api.clickup.com/api/v2/task/abc123/dependency?depends_on=def456');
    assert.strictEqual(options.method, 'DELETE');
    return {
      ok: true,
      json: async () => ({})
    };
  };

  const res = await api.removeDependency('abc123', 'def456');
  assert.deepStrictEqual(res, {});
});

test('getUnassignedTasks uses hardcoded WORKSPACE_TEAM_ID and filters human assignees', async () => {
  const api = new ClickUpAPI('fake_key');
  let capturedSpaceUrl = null;

  global.fetch = async (url, options) => {
    if (url.includes('/space?')) {
      capturedSpaceUrl = url;
      return { ok: true, json: async () => ({ spaces: [{ id: 's1' }] }) };
    }
    if (url.includes('/space/s1/list?')) {
      return { ok: true, json: async () => ({ lists: [{ id: 'l1' }] }) };
    }
    if (url.includes('/space/s1/folder?')) {
      return { ok: true, json: async () => ({ folders: [] }) };
    }
    if (url.includes('/list/l1/task?')) {
      return {
        ok: true,
        json: async () => ({
          tasks: [
            { id: 't1', name: 'Assigned Task', assignees: [{ id: 81848905 }] },
            { id: 't2', name: 'Unassigned Task', assignees: [], list: { name: 'My List' }, url: 'https://app.clickup.com/t/t2' }
          ]
        })
      };
    }
    return { ok: true, json: async () => ({}) };
  };

  const res = await api.getUnassignedTasks();
  assert.strictEqual(res.length, 1);
  assert.strictEqual(res[0].id, 't2');
  assert.ok(capturedSpaceUrl.includes('90121717552'), `Expected WORKSPACE_TEAM_ID in URL, got: ${capturedSpaceUrl}`);
});

test('uploadAttachment throws on missing args', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.uploadAttachment(), /taskId and filePath are required/);
});

test('getList throws on missing listId', async () => {
  const api = new ClickUpAPI('fake_key');
  await assert.rejects(() => api.getList(), /listId is required/);
});

test('getList fetches list details', async () => {
  const api = new ClickUpAPI('fake_key');
  global.fetch = async (url, options) => {
    assert.strictEqual(url, 'https://api.clickup.com/api/v2/list/123');
    assert.strictEqual(options?.method, undefined);
    return {
      ok: true,
      json: async () => ({ id: '123', name: 'Test List', statuses: [{ status: 'to do' }, { status: 'in progress' }] })
    };
  };
  const list = await api.getList('123');
  assert.strictEqual(list.id, '123');
  assert.strictEqual(list.statuses.length, 2);
});

test('createTask converts ISO due_date string to Unix timestamp in milliseconds', async (t) => {
  const api = new ClickUpAPI('fake-key');
  let callCount = 0;

  global.fetch = async (url, options) => {
    callCount++;
    if (callCount === 1) {
      assert.strictEqual(url, 'https://api.clickup.com/api/v2/list/123/task');
      assert.strictEqual(options.method, 'POST');
      const body = JSON.parse(options.body);
      const expectedMs = new Date('2026-07-13T00:00:00.000Z').getTime();
      assert.strictEqual(typeof body.due_date, 'number');
      assert.strictEqual(body.due_date, expectedMs);
      return { ok: true, json: async () => ({ id: 'mock-id', url: 'mock-url' }) };
    } else {
      return { ok: true, json: async () => ({}) };
    }
  };

  await api.createTask('123', 'Test Task', 'desc', 1, null, false, null, null, null, '2026-07-13');
  assert.strictEqual(callCount, 1);
});

test('createFolder throws on missing args', async () => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.createFolder(), /spaceId and name are required/);
});

test('createFolder sends correct payload', async () => {
  const api = new ClickUpAPI('fake-key');
  let capturedUrl = null;
  let capturedOptions = null;

  global.fetch = async (url, options) => {
    capturedUrl = url;
    capturedOptions = options;
    return {
      ok: true,
      json: async () => ({ id: 'folder-123', name: 'New Folder' })
    };
  };

  const res = await api.createFolder('space-789', 'New Folder');
  assert.strictEqual(capturedUrl, 'https://api.clickup.com/api/v2/space/space-789/folder');
  assert.strictEqual(capturedOptions.method, 'POST');
  const body = JSON.parse(capturedOptions.body);
  assert.strictEqual(body.name, 'New Folder');
  assert.strictEqual(res.id, 'folder-123');
  assert.strictEqual(res.name, 'New Folder');
});

test('createList throws on missing args', async () => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.createList(), /folderId and name are required/);
});

test('createList sends correct payload', async () => {
  const api = new ClickUpAPI('fake-key');
  let capturedUrl = null;
  let capturedOptions = null;

  global.fetch = async (url, options) => {
    capturedUrl = url;
    capturedOptions = options;
    return {
      ok: true,
      json: async () => ({ id: 'list-123', name: 'New List' })
    };
  };

  const res = await api.createList('folder-789', 'New List');
  assert.strictEqual(capturedUrl, 'https://api.clickup.com/api/v2/folder/folder-789/list');
  assert.strictEqual(capturedOptions.method, 'POST');
  const body = JSON.parse(capturedOptions.body);
  assert.strictEqual(body.name, 'New List');
  assert.strictEqual(res.id, 'list-123');
  assert.strictEqual(res.name, 'New List');
});

test('deleteList throws on missing args', async () => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.deleteList(), /listId is required/);
});

test('deleteList sends correct payload', async () => {
  const api = new ClickUpAPI('fake-key');
  let capturedUrl = null;
  let capturedOptions = null;

  global.fetch = async (url, options) => {
    capturedUrl = url;
    capturedOptions = options;
    return {
      ok: true,
      json: async () => ({})
    };
  };

  const res = await api.deleteList('list-123');
  assert.strictEqual(capturedUrl, 'https://api.clickup.com/api/v2/list/list-123');
  assert.strictEqual(capturedOptions.method, 'DELETE');
  assert.deepStrictEqual(res, { success: true });
});


