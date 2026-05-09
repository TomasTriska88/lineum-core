export class ClickUpAPI {
  constructor(apiKey) {
    if (!apiKey) {
      throw new Error("CLICKUP_API_KEY is required");
    }
    this.apiKey = apiKey;
    this.baseUrl = "https://api.clickup.com/api/v2";
  }

  async createTask(listId, name, description, priority) {
    if (!listId || !name) {
      throw new Error("listId and name are required to create a task");
    }

    const payload = {
      name,
      description,
      priority,
      status: "to do"
    };

    const response = await fetch(`${this.baseUrl}/list/${listId}/task`, {
      method: "POST",
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

  async getTasks(listId, status = "to do") {
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
    if (!taskId || !updateData) {
      throw new Error("taskId and updateData are required to update a task");
    }

    const response = await fetch(`${this.baseUrl}/task/${taskId}`, {
      method: "PUT",
      headers: {
        "Authorization": this.apiKey,
        "Content-Type": "application/json"
      },
      body: JSON.stringify(updateData)
    });

    if (!response.ok) {
      const errData = await response.text();
      throw new Error(`ClickUp API Error: ${response.status} - ${errData}`);
    }

    return await response.json();
  }
}
