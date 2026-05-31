import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { ClickUpAPI, normalizeText } from "./api.js";

const api = new ClickUpAPI(process.env.CLICKUP_API_KEY);

const server = new Server(
  {
    name: "lineum-clickup",
    version: "1.2.1",
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
            },
            parent_id: {
              type: "string",
              description: "Optional ID of a parent task to create this as a subtask."
            },
            is_milestone: {
              type: "boolean",
              description: "Set to true to create a native ClickUp Milestone (diamond icon)."
            },
            time_estimate_hours: {
              type: "number",
              description: "Time estimate for the task in hours."
            },
            assignees: {
              type: "array",
              items: { type: "number" },
              description: "Array of user IDs to assign to the task."
            },
            points: {
              type: "number",
              description: "Sprint Points for the task (Fibonacci: 1, 2, 3, 5, 8, 13)."
            },
            dor_comment: {
              type: "string",
              description: "MANDATORY: The DoR audit checklist text. Must cover: (1) Assignee justification, (2) research performed, (3) time estimate rationale, (4) priority justification, (5) language confirmation. The server will automatically post this as a native ClickUp comment for audit trail."
            },
            due_date: {
              type: "string",
              description: "Due date for the task as an ISO date string (YYYY-MM-DD), e.g. '2026-07-13'. Per Deadline Policy, set to the maximum legally permissible date, not an artificially compressed one."
            }
          },
          required: ["list_id", "name", "dor_comment"]
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
      },
      {
        name: "update_task",
        description: "Update general properties of an existing ClickUp task, such as its markdown description.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: {
              type: "string",
              description: "The ID of the ClickUp Task to update."
            },
            description: {
              type: "string",
              description: "The new Markdown description for the task."
            },
            status: {
              type: "string",
              description: "The new status (e.g. 'to do', 'in progress', 'paused', 'blocked', 'complete'). Setting 'complete' requires dod_audit_confirmed: true. Setting 'blocked' requires dob_audit_confirmed: true."
            },
            time_estimate_hours: {
              type: "number",
              description: "Time estimate for the task in hours."
            },
            name: {
              type: "string",
              description: "The new name of the task."
            },
            assignees_add: {
              type: "array",
              items: { type: "number" },
              description: "Array of user IDs to assign to the task."
            },
            assignees_rem: {
              type: "array",
              items: { type: "number" },
              description: "Array of user IDs to remove from the task."
            },
            points: {
              type: "number",
              description: "Sprint Points for the task."
            },
            dod_audit_confirmed: {
              type: "boolean",
              description: "REQUIRED when setting status to 'complete'. Must be true, confirming the DoD self-audit checklist has been printed in the response BEFORE this call."
            },
            dob_audit_confirmed: {
              type: "boolean",
              description: "REQUIRED when setting status to 'blocked'. Must be true, confirming the DoB self-audit checklist has been printed in the response BEFORE this call."
            },
            sou_comment: {
              type: "string",
              description: "REQUIRED when updating 'description'. SoU = Statement of Update. Summarizes what changed and why. The server auto-posts this as a typed comment (prefix: '\u{1F4DD} SoU:') BEFORE applying the description update, making the change visible in the Activity feed without needing to diff the description."
            },
            dod_comment: {
              type: "string",
              description: "REQUIRED when setting status to 'complete'. The DoD audit checklist text and final closing note detailing the resolution. The server will automatically post this as a native ClickUp comment for audit trail before closing the task."
            },
            due_date: {
              type: "string",
              description: "Due date for the task as an ISO date string (YYYY-MM-DD), e.g. '2026-07-13'. Per Deadline Policy, set to the maximum legally permissible date, not an artificially compressed one."
            },
            parent: {
              type: "string",
              description: "The ID of the parent task to move this task under. Set to null to remove parent."
            }
          },
          required: ["task_id"]
        }
      },
      {
        name: "add_comment",
        description: "Add a comment to a task.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string" },
            comment_text: { type: "string" }
          },
          required: ["task_id", "comment_text"]
        }
      },
      {
        name: "add_dependency",
        description: "Make a task wait on another task.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string", description: "The ID of the task that is waiting." },
            depends_on_task_id: { type: "string", description: "The ID of the task that is blocking it." }
          },
          required: ["task_id", "depends_on_task_id"]
        }
      },
      {
        name: "remove_dependency",
        description: "Remove a dependency between two tasks.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string", description: "The ID of the task." },
            depends_on_task_id: { type: "string", description: "The ID of the task that was blocking it." }
          },
          required: ["task_id", "depends_on_task_id"]
        }
      },
      {
        name: "add_tag",
        description: "Add a tag to a ClickUp task.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string" },
            tag_name: { type: "string" }
          },
          required: ["task_id", "tag_name"]
        }
      },
      {
        name: "get_workspace_hierarchy",
        description: "Get the full workspace hierarchy (Spaces, Folders, Lists) for the workspace.",
        inputSchema: {
          type: "object",
          properties: {
            max_depth: { type: "number", description: "Depth of hierarchy to fetch: 0 = Spaces, 1 = Spaces+Folders, 2 = Spaces+Folders+Lists. Default is 2." }
          },
          required: []
        }
      },
      {
        name: "get_space",
        description: "Get full details of a single ClickUp Space including its members and permissions.",
        inputSchema: {
          type: "object",
          properties: {
            space_id: { type: "string", description: "The ID of the ClickUp Space." }
          },
          required: ["space_id"]
        }
      },
      {
        name: "update_space",
        description: "Update Space settings, such as enabling ClickApps or toggling privacy.",
        inputSchema: {
          type: "object",
          properties: {
            space_id: { type: "string", description: "The ID of the Space." },
            features: { type: "object", description: "Optional features object to enable/disable ClickApps." },
            private: { type: "boolean", description: "Optional boolean to set Space as private (true) or public (false)." },
            members: {
              type: "array",
              items: { type: "number" },
              description: "Optional array of user IDs to grant access to a private Space."
            }
          },
          required: ["space_id"]
        }
      },
      {
        name: "get_workspace_users",
        description: "Get users in the workspace.",
        inputSchema: {
          type: "object",
          properties: {},
          required: []
        }
      },
      {
        name: "get_task",
        description: "Get full details of a single task including checklists, subtasks, dependencies, and time estimates. Use this before estimating hours to read all available task context.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string", description: "The ID of the ClickUp task." }
          },
          required: ["task_id"]
        }
      },
      {
        name: "get_task_comments",
        description: "Get all comments on a ClickUp task. Use this before estimating hours to read full task context.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string", description: "The ID of the ClickUp task." }
          },
          required: ["task_id"]
        }
      },
      {
        name: "get_unassigned_tasks",
        description: "Scans all workspace tasks and returns a list of tasks that do not have a human assignee.",
        inputSchema: {
          type: "object",
          properties: {},
          required: []
        }
      },
      {
        name: "upload_attachment",
        description: "Upload a local file as an attachment to a ClickUp task.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string", description: "The ID of the ClickUp task." },
            file_path: { type: "string", description: "The absolute path to the local file to upload." },
            file_name: { type: "string", description: "Optional explicit file name. If omitted, the base name of the path is used." }
          },
          required: ["task_id", "file_path"]
        }
      },
      {
        name: "get_list",
        description: "Get details of a list, including its available statuses.",
        inputSchema: {
          type: "object",
          properties: {
            list_id: { type: "string", description: "The ID of the ClickUp list." }
          },
          required: ["list_id"]
        }
      },
      {
        name: "update_comment",
        description: "Update the text of an existing comment on a ClickUp task.",
        inputSchema: {
          type: "object",
          properties: {
            comment_id: { type: "string", description: "The ID of the comment to update." },
            comment_text: { type: "string", description: "The new text content for the comment." }
          },
          required: ["comment_id", "comment_text"]
        }
      },
      {
        name: "create_folder",
        description: "Create a new Folder inside a ClickUp Space.",
        inputSchema: {
          type: "object",
          properties: {
            space_id: { type: "string", description: "The ID of the Space to create the folder in." },
            name: { type: "string", description: "Name of the new folder." }
          },
          required: ["space_id", "name"]
        }
      },
      {
        name: "create_list",
        description: "Create a new List inside a ClickUp Folder.",
        inputSchema: {
          type: "object",
          properties: {
            folder_id: { type: "string", description: "The ID of the Folder to create the list in." },
            name: { type: "string", description: "Name of the new list." }
          },
          required: ["folder_id", "name"]
        }
      },
      {
        name: "delete_list",
        description: "Delete an existing List in ClickUp.",
        inputSchema: {
          type: "object",
          properties: {
            list_id: { type: "string", description: "The ID of the ClickUp List to delete." }
          },
          required: ["list_id"]
        }
      },
      {
        name: "delete_task",
        description: "Delete an existing Task in ClickUp.",
        inputSchema: {
          type: "object",
          properties: {
            task_id: { type: "string", description: "The ID of the ClickUp Task to delete." }
          },
          required: ["task_id"]
        }
      }

    ]
  };
});



server.setRequestHandler(CallToolRequestSchema, async (request) => {
  if (request.params.name === "create_task") {
    let { list_id, name, description, priority, parent_id, is_milestone, time_estimate_hours, assignees, points, dor_comment, due_date } = request.params.arguments;
    name = normalizeText(name);
    description = normalizeText(description);
    dor_comment = normalizeText(dor_comment);
    try {
      // Hard gate: creating a task without an assignee is forbidden
      if (!assignees || assignees.length === 0) {
        return {
          content: [{ type: "text", text: "🚫 DoR Gate: Cannot create task without at least one assignee.\n\nCall get_workspace_users first to resolve the correct user ID, then retry with assignees: [<id>]." }],
          isError: true
        };
      }
      // Hard gate: DoR comment is mandatory
      if (!dor_comment || !dor_comment.trim()) {
        return {
          content: [{ type: "text", text: "🚫 DoR Gate: Cannot create task without a dor_comment.\n\nProvide the DoR audit checklist text covering: assignee justification, research performed, time estimate rationale, priority justification, and language confirmation." }],
          isError: true
        };
      }
      const data = await api.createTask(list_id, name, description, priority, parent_id, is_milestone, time_estimate_hours, assignees, points, due_date);
      // Automatically post the DoR audit comment — no separate step needed
      await api.addComment(data.id, dor_comment);
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
      const summary = tasks.map(t => {
        let deps = "";
        if (t.dependencies && t.dependencies.length > 0) {
           const blockers = t.dependencies.filter(d => d.task_id === t.id).map(d => d.depends_on);
           if (blockers.length > 0) deps = ` [BLOCKED BY: ${blockers.join(', ')}]`;
        }
        return `- [ID: ${t.id}] [Status: ${t.status.status}] [Priority ${t.priority?.id || '?'}] ${t.name}${deps}`;
      }).join('\n');
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

  if (request.params.name === "update_task") {
    let { task_id, description, status, time_estimate_hours, name, assignees_add, assignees_rem, points, dod_audit_confirmed, dob_audit_confirmed, sou_comment, due_date, dod_comment, parent } = request.params.arguments;
    name = normalizeText(name);
    description = normalizeText(description);
    sou_comment = normalizeText(sou_comment);
    dod_comment = normalizeText(dod_comment);
    try {
      let taskDetails = null;
      let currentStatus = "";
      let taskName = process.env.MOCK_CLICKUP_TASK_NAME || "";
      if (process.env.MOCK_CLICKUP_TASK_STATUS) {
        currentStatus = process.env.MOCK_CLICKUP_TASK_STATUS.toLowerCase();
      } else {
        try {
          taskDetails = await api.getTask(task_id);
          currentStatus = taskDetails.status ? taskDetails.status.status.toLowerCase() : "";
          if (taskDetails && taskDetails.name) {
            taskName = taskDetails.name;
          }
        } catch (e) {
          if (process.env.CLICKUP_API_KEY === "test-key") {
            currentStatus = "in progress";
          } else {
            throw e;
          }
        }
      }

      // Hard gate: closing a task without DoD audit is forbidden
      if (status === "complete") {
        if (dod_audit_confirmed !== true) {
          return {
            content: [{ type: "text", text: "🚫 DoD Gate: Cannot set status to 'complete' without dod_audit_confirmed: true.\n\nYou MUST first print the DoD audit checklist in your response:\n\n### 🛡️ DoD Audit\n- [ ] Documentation: ...\n- [ ] Tests: ...\n- [ ] ClickUp: ...\n- [ ] Cleanliness: ...\n- [ ] Comment Trail (SoU): ...\n\nThen retry this call with dod_audit_confirmed: true." }],
            isError: true
          };
        }
        if (!dod_comment || !dod_comment.trim()) {
          return {
            content: [{ type: "text", text: "🚫 DoD Gate: Cannot set status to 'complete' without a dod_comment.\n\nProvide the DoD audit checklist and final closing note as the 'dod_comment' parameter, e.g. covering documentation, tests, cleanliness, and Git push verification." }],
            isError: true
          };
        }

        // Research Gate check: Research/Exploration/Preparation/Draft tasks cannot be closed without user approval
        const isResearchOrPrep = /research|exploration|prepare|preparation|draft/i.test(taskName);
        if (isResearchOrPrep) {
          const hasUserApproval = dod_comment.toLowerCase().includes("user approved: yes") || 
                                 dod_comment.toLowerCase().includes("user approved:yes") ||
                                 dod_comment.toLowerCase().includes("user approved closure: yes") ||
                                 dod_comment.toLowerCase().includes("user approved closure:yes");
          if (!hasUserApproval) {
            return {
              content: [{ type: "text", text: `🚫 Research Gate: Task '${taskName}' is classified as a research, exploration, or preparation/draft task. The agent is strictly forbidden from marking such tasks as complete without explicit user approval. Please verify that the user has explicitly requested or approved this closure, and add 'User approved: Yes' to your dod_comment.` }],
              isError: true
            };
          }
        }
      }
      // Hard gate: blocking a task without DoB audit is forbidden
      if (status === "blocked" && dob_audit_confirmed !== true) {
        return {
          content: [{ type: "text", text: "🚫 DoB Gate: Cannot set status to 'blocked' without dob_audit_confirmed: true.\n\nYou MUST first print the DoB audit checklist in your response:\n\n### 🧱 DoB Audit\n- [ ] Blocker identified (linked): ...\n- [ ] Session summary comment: ...\n- [ ] Blocker task is DoR-ready: ...\n- [ ] Compliance checklist: ...\n- [ ] Task description updated: ...\n\nThen retry this call with dob_audit_confirmed: true." }],
          isError: true
        };
      }

      const isTransitioningToActive = status !== undefined && status.toLowerCase() !== "to do";
      const isCurrentlyToDo = currentStatus === "to do";

      // Hard gate: updating description without SoU/Plan comment is forbidden
      if (description !== undefined && (!sou_comment || !sou_comment.trim())) {
        const errorText = isCurrentlyToDo && !isTransitioningToActive
          ? "🚫 Plan Gate: Cannot update 'description' without sou_comment.\n\nProvide a Statement of Plan (Plan) summarizing what changed in the specification/scoping. Example:\n\n  sou_comment: 'Updated acceptance criteria to include director loan reconciliation step.'\n\nThe server will auto-post this as a typed comment prefixed with '📝 Plan:' before applying the description change."
          : "🚫 SoU Gate: Cannot update 'description' without sou_comment.\n\nProvide a Statement of Update (SoU) summarizing what changed and why. Example:\n\n  sou_comment: '📝 SoU: Updated acceptance criteria to include director loan reconciliation step.'\n\nThe server will auto-post this as a typed comment before applying the description change.";
        return {
          content: [{ type: "text", text: errorText }],
          isError: true
        };
      }

      // Auto-post comment BEFORE applying description update
      if (description !== undefined && sou_comment && sou_comment.trim()) {
        const prefix = (isCurrentlyToDo && !isTransitioningToActive) ? "\u{1F4DD} Plan: " : "\u{1F4DD} SoU: ";
        const cleanComment = sou_comment.startsWith("\u{1F4DD} Plan: ") || sou_comment.startsWith("\u{1F4DD} SoU: ") || sou_comment.startsWith("📝 Plan: ") || sou_comment.startsWith("📝 SoU: ")
          ? sou_comment.replace(/^(\u{1F4DD}|📝)\s*(Plan|SoU):\s*/i, "")
          : sou_comment;
        const fullComment = prefix + cleanComment;
        await api.addComment(task_id, fullComment);
      }

      // Auto-post DoD comment BEFORE closing task
      if (status === "complete" && dod_comment && dod_comment.trim()) {
        await api.addComment(task_id, dod_comment);
      }
      
      const updateData = {};
      if (description !== undefined) updateData.description = description;
      if (status !== undefined) updateData.status = status;
      if (time_estimate_hours !== undefined) updateData.time_estimate_hours = time_estimate_hours;
      if (name !== undefined) updateData.name = name;
      if (assignees_add !== undefined) updateData.assignees_add = assignees_add;
      if (assignees_rem !== undefined) updateData.assignees_rem = assignees_rem;
      if (points !== undefined) updateData.points = points;
      if (due_date !== undefined) updateData.due_date = due_date;
      if (parent !== undefined) updateData.parent = parent;
      
      await api.updateTask(task_id, updateData);
      return {
        content: [{ type: "text", text: `Task updated successfully.` }]
      };
    } catch (e) {
      return {
        content: [{ type: "text", text: e.message }],
        isError: true
      };
    }
  }

  if (request.params.name === "add_comment") {
    let { task_id, comment_text } = request.params.arguments;
    comment_text = normalizeText(comment_text);
    try {
      // Enforce: Cannot post SoU comment if the task is in 'to do' status.
      if (comment_text.trim().startsWith("📝 SoU:") || comment_text.trim().startsWith("\u{1F4DD} SoU:")) {
        let currentStatus = "";
        if (process.env.MOCK_CLICKUP_TASK_STATUS) {
          currentStatus = process.env.MOCK_CLICKUP_TASK_STATUS.toLowerCase();
        } else {
          try {
            const taskDetails = await api.getTask(task_id);
            currentStatus = taskDetails.status ? taskDetails.status.status.toLowerCase() : "";
          } catch (e) {
            if (process.env.CLICKUP_API_KEY === "test-key") {
              currentStatus = "in progress";
            } else {
              throw e;
            }
          }
        }
        if (currentStatus === "to do") {
          return {
            content: [{ type: "text", text: "🚫 SoU Gate: Cannot post a Statement of Update (SoU) comment on a task in 'to do' status. Progress updates are only permitted on active tasks." }],
            isError: true
          };
        }
      }

      await api.addComment(task_id, comment_text);
      return { content: [{ type: "text", text: "Comment added successfully." }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "add_dependency") {
    const { task_id, depends_on_task_id } = request.params.arguments;
    try {
      await api.addDependency(task_id, depends_on_task_id);
      return { content: [{ type: "text", text: `Dependency added successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "remove_dependency") {
    const { task_id, depends_on_task_id } = request.params.arguments;
    try {
      await api.removeDependency(task_id, depends_on_task_id);
      return { content: [{ type: "text", text: `Dependency removed successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "add_tag") {
    const { task_id, tag_name } = request.params.arguments;
    try {
      await api.addTag(task_id, tag_name);
      return { content: [{ type: "text", text: `Tag added successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_workspace_hierarchy") {
    const { max_depth } = request.params.arguments;
    try {
      const hierarchy = await api.getWorkspaceHierarchy(max_depth !== undefined ? max_depth : 2);
      return { content: [{ type: "text", text: JSON.stringify(hierarchy, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_space") {
    const { space_id } = request.params.arguments;
    try {
      const space = await api.getSpace(space_id);
      return { content: [{ type: "text", text: JSON.stringify(space, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "update_space") {
    const { space_id, features, private: isPrivate, members } = request.params.arguments;
    try {
      const payload = {};
      if (features !== undefined) payload.features = features;
      if (isPrivate !== undefined) payload.private = isPrivate;
      if (members !== undefined) payload.members = members;
      await api.updateSpace(space_id, payload);
      return { content: [{ type: "text", text: `Space updated successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_workspace_users") {
    try {
      const users = await api.getWorkspaceUsers();
      return { content: [{ type: "text", text: JSON.stringify(users, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_task") {
    const { task_id } = request.params.arguments;
    try {
      const task = await api.getTask(task_id);
      return { content: [{ type: "text", text: JSON.stringify(task, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_task_comments") {
    const { task_id } = request.params.arguments;
    try {
      const comments = await api.getTaskComments(task_id);
      return { content: [{ type: "text", text: JSON.stringify(comments, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_unassigned_tasks") {
    try {
      const result = await api.getUnassignedTasks();
      return { content: [{ type: "text", text: JSON.stringify(result, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "upload_attachment") {
    const { task_id, file_path, file_name } = request.params.arguments;
    try {
      const data = await api.uploadAttachment(task_id, file_path, file_name);
      return { content: [{ type: "text", text: `Attachment uploaded successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "get_list") {
    const { list_id } = request.params.arguments;
    try {
      const data = await api.getList(list_id);
      return { content: [{ type: "text", text: JSON.stringify(data, null, 2) }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "update_comment") {
    let { comment_id, comment_text } = request.params.arguments;
    comment_text = normalizeText(comment_text);
    try {
      await api.updateComment(comment_id, comment_text);
      return { content: [{ type: "text", text: `Comment ${comment_id} updated successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "create_folder") {
    let { space_id, name } = request.params.arguments;
    name = normalizeText(name);
    try {
      const data = await api.createFolder(space_id, name);
      return { content: [{ type: "text", text: `Folder created. ID: ${data.id}, Name: ${data.name}` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "create_list") {
    let { folder_id, name } = request.params.arguments;
    name = normalizeText(name);
    try {
      const data = await api.createList(folder_id, name);
      return { content: [{ type: "text", text: `List created. ID: ${data.id}, Name: ${data.name}` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "delete_list") {
    const { list_id } = request.params.arguments;
    try {
      await api.deleteList(list_id);
      return { content: [{ type: "text", text: `List ${list_id} deleted successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }

  if (request.params.name === "delete_task") {
    const { task_id } = request.params.arguments;
    try {
      await api.deleteTask(task_id);
      return { content: [{ type: "text", text: `Task ${task_id} deleted successfully.` }] };
    } catch (e) { return { content: [{ type: "text", text: e.message }], isError: true }; }
  }


  throw new Error("Tool not found");
});

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("ClickUp MCP server running on stdio");
