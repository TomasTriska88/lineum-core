import test from 'node:test';
import assert from 'node:assert';
import { ClickUpAPI } from './api.js';

test('ClickUpAPI constructor', (t) => {
  assert.throws(() => new ClickUpAPI(), /CLICKUP_API_KEY is required/);
  const api = new ClickUpAPI('fake-key');
  assert.strictEqual(api.apiKey, 'fake-key');
});

test('createTask throws on missing args', async (t) => {
  const api = new ClickUpAPI('fake-key');
  await assert.rejects(() => api.createTask(), /listId and name are required/);
});

test('createTask sends correct payload', async (t) => {
  const api = new ClickUpAPI('fake-key');
  
  // Mock fetch
  global.fetch = async (url, options) => {
    assert.strictEqual(url, 'https://api.clickup.com/api/v2/list/123/task');
    assert.strictEqual(options.method, 'POST');
    assert.strictEqual(options.headers['Authorization'], 'fake-key');
    
    const body = JSON.parse(options.body);
    assert.strictEqual(body.name, 'Test Task');
    assert.strictEqual(body.priority, 1);
    
    return {
      ok: true,
      json: async () => ({ id: 'mock-id', url: 'mock-url' })
    };
  };

  const res = await api.createTask('123', 'Test Task', 'desc', 1);
  assert.strictEqual(res.id, 'mock-id');
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
    assert.strictEqual(body.description, 'New Context');
    
    return {
      ok: true,
      json: async () => ({ id: 'task-123' })
    };
  };

  const res = await api.updateTask('task-123', { description: 'New Context' });
  assert.strictEqual(res.id, 'task-123');
});
