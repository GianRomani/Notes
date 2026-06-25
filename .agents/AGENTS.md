# Antigravity Local Customization Rules

These rules apply to this workspace and project.

## 📊 Linear & GitHub Workflow Alignment

- **Linear Task Creation:** Every time the user asks to add something to the todo/tasks list, the agent must immediately check and ensure a corresponding issue is created in Linear (if not already present).
- **Linear Task Enrichment:** When brainstorming a task or creating a new note/ADR, the agent must update the corresponding Linear task description with details on what is to be achieved, how, and provide links to the relevant decision logs/ADR files in the workspace.
- **GitHub PR Linking:** When a new Pull Request is opened, the agent must ensure it links to and updates the corresponding Linear issue so the PR status is tracked directly within Linear.
- **Default Assignee:** All newly created or updated tasks in Linear must be assigned to the user by default, unless explicitly specified otherwise.
