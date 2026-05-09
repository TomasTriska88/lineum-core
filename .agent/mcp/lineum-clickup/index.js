import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { ClickUpAPI } from "./api.js";

const api = new ClickUpAPI(process.env.CLICKUP_API_KEY);

const server = new Server(
  {
    name: "lineum-clickup",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "create_task",
        description: "Create a new task in ClickUp.",
        inputSchema: {
          type: "object",
          properties: {
            list_id: {
              type: "string",
              description: "The ID of the ClickUp List to create the task in."
            },
            name: {
              type: "string",
              description: "Name of the task."
            },
            description: {
              type: "string",
              description: "Markdown description of the task."
            },
            priority: {
              type: "number",
              description: "1 (Urgent), 2 (High), 3 (Normal), 4 (Low)."
            }
          },
          required: ["list_id", "name"]
        }
      },
      {
        name: "get_tasks",
        description: "Get tasks from a ClickUp List, ordered by priority.",
        inputSchema: {
          type: "object",
          properties: {
            list_id: {
              type: "string",
              description: "The ID of the ClickUp List to fetch tasks from."
            },
            status: {
              type: "string",
              description: "Status filter. Defaults to 'to do'."
            }
          },
          required: ["list_id"]
        }
      },
      {
        name: "update_task_priority",
        description: "Update the priority of an existing ClickUp task.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: {
              type: "string",
              description: "The ID of the ClickUp Task to update."
            },
            priority: {
              type: "number",
              description: "1 (Urgent), 2 (High), 3 (Normal), 4 (Low)."
            }
          },
          required: ["task_id", "priority"]
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "create_task") {
    const { list_id, name, description, priority } = request.params.arguments;
    try {
      const data = await api.createTask(list_id, name, description, priority);
      return {
        content: [{ type: "text", text: `Task created successfully. URL: ${data.url}` }]
      };
    } catch (e) {
      return {
        content: [{ type: "text", text: e.message }],
        isError: true
      };
    }
  }

  if (request.params.name === "get_tasks") {
    const { list_id, status } = request.params.arguments;
    try {
      const tasks = await api.getTasks(list_id, status);
      const summary = tasks.map(t => `- [ID: ${t.id}] [Priority ${t.priority?.id || '?'}] ${t.name}`).join('\n');
      return {
        content: [{ type: "text", text: summary || "No tasks found." }]
      };
    } catch (e) {
      return {
        content: [{ type: "text", text: e.message }],
        isError: true
      };
    }
  }

  if (request.params.name === "update_task_priority") {
    const { task_id, priority } = request.params.arguments;
    try {
      const data = await api.updateTaskPriority(task_id, priority);
      return {
        content: [{ type: "text", text: `Task priority updated successfully to ${priority}.` }]
      };
    } catch (e) {
      return {
        content: [{ type: "text", text: e.message }],
        isError: true
      };
    }
  }

  throw new Error("Tool not found");
});

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("Lineum ClickUp MCP server running on stdio");
