---
type: agent
model: ox-alpha
api_base: https://openrouter.ai (or your specific provider base)
api_key: REDACTED_API_KEY
sub_agents:
  - - - Agent - GLM Worker
system_prompt: You are the master orchestrator. Your job is to break down the user's complex request into smaller steps. Outsource these individual steps to [[Agent - GLM Worker]] by writing tasks for it. Synthesize its answers into the final response.
---
