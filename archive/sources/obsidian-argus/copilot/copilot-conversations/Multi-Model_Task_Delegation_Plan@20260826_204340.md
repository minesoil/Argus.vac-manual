---
epoch: 1787748220193
modelKey: google/gemini-2.5-flash|openrouterai
tags:
  - copilot-conversation
topic: Multi-Model Task Delegation Plan
---

**user**: Ox Alpha: Plan this task, delegate text and YAML formatting to GLM 5.2 (z-ai/glm-5.2:free), route code and logic checks to Nemotron 3 (nvidia/nemotron-3-ultra-550b-a55b:free), and return a clean final note for Justin.

make it so that my prompt above will always be read first before anything
[Timestamp: 2026/08/26 20:43:40]

**ai**: 
<think>User wants a persistent instruction that their prompt is always read first. I can't persist instructions across chats, but I can suggest putting it in Obsidian Copilot settings (custom system prompt / "user system prompt"). Also they asked me to plan the task and produce a final note — but there's no actual task content. Clarify.</think>I can help with this! A quick clarification first: **I can't permanently save instructions across conversations** — each chat starts fresh. But here's how to make your prompt load first every time in Obsidian:

### Make it persistent
1. Open **Obsidian Settings → Copilot → Advanced → User System Prompt**.
2. Paste this block at the very top of that field — anything there is injected before all other context on every message:

```
PRIORITY INSTRUCTION — READ FIRST:
- Plan the user's task before executing.
- Delegate text + YAML formatting to GLM 5.2 (z-ai/glm-5.2:free).
- Route code and logic checks to Nemotron 3 (nvidia/nemotron-3-ultra-550b-a55b:free).
- Return a clean final note for Justin.
```

Alternatively, you can create it as a **Copilot command/preset** so you invoke it with one click.

### One thing to note about the routing
Within this chat, I'm ox-alpha — I don't have live access to call GLM 5.2 or Nemotron 3 as sub-models myself. What I *can* do is simulate the workflow: plan the task, draft the text/YAML sections the way GLM would format them, and run logic/code review passes Nemotron-style before delivering Justin's note.

### Ready when you are
To actually execute the task, just tell me:
- What the task/note content is,
- Any vault notes to include (@vault),
- Where the note should go / what to name it.

Then I'll deliver the clean final note for Justin in one pass.
[Timestamp: 2026/08/26 20:43:56]