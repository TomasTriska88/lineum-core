// The default workspace team ID.
const WORKSPACE_TEAM_ID = "90121717552";

// Normalize text: unescape literal \n and \t sequences sent by the MCP framework
export function normalizeText(text) {
  if (typeof text !== 'string') return text;
  return text.replace(/\\n/g, '\n').replace(/\\t/g, '\t');
}

export class ClickUpAPI {
  constructor(apiKey) {
    this.apiKey = apiKey;
    this.baseUrl = "https://api.clickup.com/api/v2";
  }

  requireAuth() {
    if (!this.apiKey) {
      throw new Error("CLICKUP_API_KEY environment variable is not configured. Please add it to your MCP settings.");
    }
  }

  hasCzechChars(text) {
    if (!text) return false;
    // Basic regex for common Czech-specific diacritics
    return /[ěščřžýáíéůúťďňĚŠČŘŽÝÁÍÉŮÚŤĎŇ]/.test(text);
  }

  async createTask(listId, name, description, priority, parentId = null, isMilestone = false, timeEstimateHours = null, assignees = null, points = null, dueDate = null) {
    this.requireAuth();
    if (!listId || !name) {
      throw new Error("listId and name are required to create a task");
    }

    const payload = {
      name,
      description,
      priority,
      status: "to do",
      parent: parentId
    };

    if (isMilestone) {
      payload.custom_item_id = 1;
    }
    
    if (timeEstimateHours) {
      payload.time_estimate = Math.round(timeEstimateHours * 3600000);
    }
    
    if (assignees && Array.isArray(assignees)) {
      payload.assignees = assignees;
    }

    if (dueDate !== null && dueDate !== undefined && typeof dueDate === 'string') {
      payload.due_date = new Date(dueDate + 'T00:00:00.000Z').getTime();
    }

    let response = await fetch(`${this.baseUrl}/list/${listId}/task`, {
      method: "POST",
      headers: {
        "Authorization": this.apiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errData = await response.text();
      if (response.status === 400 && errData.includes("ITEM_417") && payload.assignees && payload.assignees.length > 1) {
        console.warn(`[ClickUpAPI] Multiple assignees not enabled in this space. Falling back to the first assignee: ${payload.assignees[0]}`);
        payload.assignees = [payload.assignees[0]];
        response = await fetch(`${this.baseUrl}/list/${listId}/task`, {
          method: "POST",
          headers: {
            "Authorization": this.apiKey,
            "Content-Type": "application/json"
          },
          body: JSON.stringify(payload)
        });
        if (!response.ok) {
          throw new Error(`ClickUp API Error (after fallback): ${response.status} - ${await response.text()}`);
        }
      } else {
        throw new Error(`ClickUp API Error: ${response.status} - ${errData}`);
      }
    }

    const task = await response.json();

    // Immediately set Sprint Points if provided — ClickUp does not support `points` in the POST body,
    // only via a subsequent PUT call. This ensures the pre-flight checklist is fully satisfied natively.
    if (points !== null && points !== undefined) {
      const ptsResponse = await fetch(`${this.baseUrl}/task/${task.id}`, {
        method: "PUT",
        headers: {
          "Authorization": this.apiKey,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ points })
      });
      if (!ptsResponse.ok) {
        console.warn(`[ClickUpAPI] Task created but failed to set sprint points: ${await ptsResponse.text()}`);
      }
    }

    return task;
  }

  async getTasks(listId, status = "to do") {
    this.requireAuth();
    if (!listId) {
      throw new Error("listId is required to get tasks");
    }

    let url = `${this.baseUrl}/list/${listId}/task`;
    if (status) {
      url += `?statuses%5B%5D=${encodeURIComponent(status)}`;
    }

    const response = await fetch(url, {
      method: "GET",
      headers: {
        "Authorization": this.apiKey
      }
    });

    if (!response.ok) {
      const errData = await response.text();
      throw new Error(`ClickUp API Error: ${response.status} - ${errData}`);
    }

    const data = await response.json();
    let tasks = data.tasks || [];
    
    // Sort tasks in JS to avoid ClickUp API 500 error (ITEMV2_003) on order_by=priority
    // ClickUp priority: 1 = Urgent, 2 = High, 3 = Normal, 4 = Low. Null means no priority (lowest).
    tasks.sort((a, b) => {
      const pA = a.priority ? parseInt(a.priority.id) : 99;
      const pB = b.priority ? parseInt(b.priority.id) : 99;
      return pA - pB;
    });

    return tasks;
  }

  async updateTaskPriority(taskId, priority) {
    this.requireAuth();
    if (!taskId || !priority) {
      throw new Error("taskId and priority are required to update a task");
    }

    const payload = { priority };

    const response = await fetch(`${this.baseUrl}/task/${taskId}`, {
      method: "PUT",
      headers: {
        "Authorization": this.apiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errData = await response.text();
      throw new Error(`ClickUp API Error: ${response.status} - ${errData}`);
    }

    return await response.json();
  }

  async updateTask(taskId, updateData) {
    this.requireAuth();
    if (!taskId || !updateData) {
      throw new Error("taskId and updateData are required");
    }

    const payload = { ...updateData };
    if (payload.assignees_add || payload.assignees_rem) {
      payload.assignees = {};
      if (payload.assignees_add) payload.assignees.add = payload.assignees_add;
      if (payload.assignees_rem) payload.assignees.rem = payload.assignees_rem;
      delete payload.assignees_add;
      delete payload.assignees_rem;
    }
    if (payload.description !== undefined) {
      payload.markdown_description = payload.description;
      delete payload.description;
    }
    if (payload.time_estimate_hours !== undefined) {
      payload.time_estimate = Math.round(payload.time_estimate_hours * 3600000);
      delete payload.time_estimate_hours;
    }
    // Accept ISO date string (YYYY-MM-DD) and convert to Unix timestamp in milliseconds.
    // ClickUp requires due_date as a Unix ms timestamp.
    if (payload.due_date !== undefined && typeof payload.due_date === 'string') {
      payload.due_date = new Date(payload.due_date + 'T00:00:00.000Z').getTime();
    }
    // points is passed through directly in the payload to the ClickUp API

    let response = await fetch(`${this.baseUrl}/task/${taskId}`, {
      method: "PUT",
      headers: {
        "Authorization": this.apiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      const errData = await response.text();
      if (response.status === 400 && errData.includes("ITEM_417") && payload.assignees && payload.assignees.add && payload.assignees.add.length > 1) {
        console.warn(`[ClickUpAPI] Multiple assignees not enabled in this space. Falling back to the first assignee: ${payload.assignees.add[0]}`);
        payload.assignees.add = [payload.assignees.add[0]];
        response = await fetch(`${this.baseUrl}/task/${taskId}`, {
          method: "PUT",
          headers: {
            "Authorization": this.apiKey,
            "Content-Type": "application/json"
          },
          body: JSON.stringify(payload)
        });
        if (!response.ok) {
          throw new Error(`ClickUp API Error (after fallback): ${response.status} - ${await response.text()}`);
        }
      } else {
        throw new Error(`ClickUp API Error: ${response.status} - ${errData}`);
      }
    }

    return await response.json();
  }

  async addDependency(taskId, dependsOnTaskId) {
    this.requireAuth();
    if (!taskId || !dependsOnTaskId) throw new Error("taskId and dependsOnTaskId required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}/dependency`, {
      method: "POST",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify({ depends_on: dependsOnTaskId })
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async removeDependency(taskId, dependsOnTaskId) {
    this.requireAuth();
    if (!taskId || !dependsOnTaskId) throw new Error("taskId and dependsOnTaskId required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}/dependency?depends_on=${dependsOnTaskId}`, {
      method: "DELETE",
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async addComment(taskId, commentText) {
    this.requireAuth();
    if (!taskId || !commentText) throw new Error("taskId and commentText required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}/comment`, {
      method: "POST",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify({ comment_text: commentText })
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async addTag(taskId, tagName) {
    this.requireAuth();
    if (!taskId || !tagName) throw new Error("taskId and tagName required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}/tag/${encodeURIComponent(tagName)}`, {
      method: "POST",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" }
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async getWorkspaceHierarchy(maxDepth = 2) {
    this.requireAuth();
    const spacesRes = await fetch(`${this.baseUrl}/team/${WORKSPACE_TEAM_ID}/space?archived=false`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!spacesRes.ok) throw new Error(`API Error: ${await spacesRes.text()}`);
    const spacesData = await spacesRes.json();
    let hierarchy = [];
    for (const space of spacesData.spaces) {
      let spaceObj = { id: space.id, name: space.name, folders: [], lists: [] };
      if (maxDepth >= 1) {
        const foldersRes = await fetch(`${this.baseUrl}/space/${space.id}/folder?archived=false`, {
          headers: { "Authorization": this.apiKey }
        });
        const foldersData = await foldersRes.json();
        for (const folder of foldersData.folders) {
          let folderObj = { id: folder.id, name: folder.name, lists: [] };
          if (maxDepth >= 2) {
            const listsRes = await fetch(`${this.baseUrl}/folder/${folder.id}/list?archived=false`, {
              headers: { "Authorization": this.apiKey }
            });
            const listsData = await listsRes.json();
            folderObj.lists = listsData.lists.map(l => ({ id: l.id, name: l.name }));
          }
          spaceObj.folders.push(folderObj);
        }
        const spaceListsRes = await fetch(`${this.baseUrl}/space/${space.id}/list?archived=false`, {
          headers: { "Authorization": this.apiKey }
        });
        const spaceListsData = await spaceListsRes.json();
        spaceObj.lists = spaceListsData.lists.map(l => ({ id: l.id, name: l.name }));
      }
      hierarchy.push(spaceObj);
    }
    return hierarchy;
  }

  async getSpace(spaceId) {
    this.requireAuth();
    if (!spaceId) throw new Error("spaceId is required");
    const response = await fetch(`${this.baseUrl}/space/${spaceId}`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`API Error: ${await response.text()}`);
    return await response.json();
  }

  async updateList(listId, updateData) {
    this.requireAuth();
    if (!listId || !updateData) throw new Error("listId and updateData are required");
    const response = await fetch(`${this.baseUrl}/list/${listId}`, {
      method: "PUT",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(updateData)
    });
    if (!response.ok) throw new Error(`API Error: ${await response.text()}`);
    return await response.json();
  }

  async deleteList(listId) {
    this.requireAuth();
    if (!listId) throw new Error("listId is required");
    const response = await fetch(`${this.baseUrl}/list/${listId}`, {
      method: "DELETE",
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`API Error: ${await response.text()}`);
    return { success: true };
  }

  async deleteTask(taskId) {
    this.requireAuth();
    if (!taskId) throw new Error("taskId is required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}`, {
      method: "DELETE",
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`API Error: ${await response.text()}`);
    return { success: true };
  }

  async getList(listId) {
    this.requireAuth();
    if (!listId) throw new Error("listId is required");
    const response = await fetch(`${this.baseUrl}/list/${listId}`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`API Error: ${await response.text()}`);
    return await response.json();
  }

  async updateSpace(spaceId, updateData) {
    this.requireAuth();
    if (!spaceId || !updateData) throw new Error("spaceId and updateData are required");
    
    // Safety guard: The ClickUp API wipes the space name if it is not explicitly provided in a PUT request.
    if (!updateData.name) {
      const currentSpace = await this.getSpace(spaceId);
      if (currentSpace && currentSpace.name) {
        updateData.name = currentSpace.name;
      }
    }

    const response = await fetch(`${this.baseUrl}/space/${spaceId}`, {
      method: "PUT",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify(updateData)
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }
  async getWorkspaceUsers() {
    this.requireAuth();
    const response = await fetch(`${this.baseUrl}/team`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`API Error: ${await response.text()}`);
    const data = await response.json();
    const team = data.teams.find(t => t.id === WORKSPACE_TEAM_ID);
    if (!team) throw new Error("Team not found");
    return team.members.map(m => m.user);
  }

  async getTask(taskId) {
    this.requireAuth();
    if (!taskId) throw new Error("taskId is required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}?include_subtasks=true`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async getTaskComments(taskId) {
    this.requireAuth();
    if (!taskId) throw new Error("taskId is required");
    const response = await fetch(`${this.baseUrl}/task/${taskId}/comment`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    const data = await response.json();
    return data.comments || [];
  }

  async getUnassignedTasks() {
    this.requireAuth();

    const SYSTEM_ID = 296638265;

    const spacesRes = await fetch(`${this.baseUrl}/team/${WORKSPACE_TEAM_ID}/space?archived=false`, {
      headers: { "Authorization": this.apiKey }
    });
    if (!spacesRes.ok) throw new Error(`ClickUp API Error: ${spacesRes.status}`);
    const spacesData = await spacesRes.json();

    let allListIds = [];
    for (const space of spacesData.spaces) {
      const sl = await fetch(`${this.baseUrl}/space/${space.id}/list?archived=false`, { headers: { "Authorization": this.apiKey } });
      const slData = await sl.json();
      if (slData.lists) allListIds.push(...slData.lists.map(l => l.id));
      const sf = await fetch(`${this.baseUrl}/space/${space.id}/folder?archived=false`, { headers: { "Authorization": this.apiKey } });
      const sfData = await sf.json();
      for (const f of (sfData.folders || [])) {
        const fl = await fetch(`${this.baseUrl}/folder/${f.id}/list?archived=false`, { headers: { "Authorization": this.apiKey } });
        const flData = await fl.json();
        if (flData.lists) allListIds.push(...flData.lists.map(l => l.id));
      }
    }

    let unassignedTasks = [];

    for (const listId of allListIds) {
      const tasksRes = await fetch(`${this.baseUrl}/list/${listId}/task?subtasks=true&include_closed=false`, {
        headers: { "Authorization": this.apiKey }
      });
      if (!tasksRes.ok) continue;
      const tasksData = await tasksRes.json();

      for (const task of (tasksData.tasks || [])) {
        const hasHumanAssignee = task.assignees && task.assignees.some(a => a.id !== SYSTEM_ID);
        if (!hasHumanAssignee) {
          unassignedTasks.push({
            id: task.id,
            name: task.name,
            list: task.list ? task.list.name : "Unknown",
            url: task.url
          });
        }
      }
    }

    return unassignedTasks;
  }

  async uploadAttachment(taskId, filePath, fileName) {
    this.requireAuth();
    if (!taskId || !filePath) throw new Error("taskId and filePath are required");
    
    const fs = await import('fs');
    const path = await import('path');
    
    if (!fs.existsSync(filePath)) {
      throw new Error(`File not found at path: ${filePath}`);
    }
    
    const fileBuffer = fs.readFileSync(filePath);
    const blob = new Blob([fileBuffer]);
    
    const formData = new FormData();
    formData.append("attachment", blob, fileName || path.basename(filePath));
    
    const response = await fetch(`${this.baseUrl}/task/${taskId}/attachment`, {
      method: "POST",
      headers: { 
        "Authorization": this.apiKey
      },
      body: formData
    });
    
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async updateComment(commentId, commentText) {
    this.requireAuth();
    if (!commentId || !commentText) throw new Error("commentId and comment_text are required");
    const response = await fetch(`${this.baseUrl}/comment/${commentId}`, {
      method: "PUT",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify({ comment_text: commentText })
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return { success: true };
  }

  async createFolder(spaceId, name) {
    this.requireAuth();
    if (!spaceId || !name) throw new Error("spaceId and name are required");
    const response = await fetch(`${this.baseUrl}/space/${spaceId}/folder`, {
      method: "POST",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify({ name })
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }

  async createList(folderId, name) {
    this.requireAuth();
    if (!folderId || !name) throw new Error("folderId and name are required");
    const response = await fetch(`${this.baseUrl}/folder/${folderId}/list`, {
      method: "POST",
      headers: { "Authorization": this.apiKey, "Content-Type": "application/json" },
      body: JSON.stringify({ name })
    });
    if (!response.ok) throw new Error(`ClickUp API Error: ${response.status} - ${await response.text()}`);
    return await response.json();
  }
}
