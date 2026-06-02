Created: 2026-06-02 09:14
#quicknote

A **managed agent harness** productises [[Harness Engineering]] by replacing the bespoke agent build process with a configuration-based deployment. AWS launched such a harness for **Bedrock AgentCore**, documented through Heeki Park's work on his Loom agent platform. The managed approach trades flexibility for speed: a managed-harness deployment completes in roughly 20 seconds against about a minute for a hand-built agent.

## Deploy-Time vs Run-Time Configuration

The harness exposes configuration at two points, where the deploy-time settings act as defaults and run-time settings override them.

- **Deploy time** (`create-harness`): system prompt, model, `max-iterations`, `max-tokens`, tools (including remote [[MCP Protocol|MCP]] servers), and memory resources.
- **Run time** (`invoke_harness`): per-invocation overrides for the model and for attached tools, allowing an end user to select a preferred model from an allow-list or enable a connector on demand.

This mirrors the hand-built pattern in Loom, where an `AGENT_CONFIG_JSON` payload conditionally enables MCP servers, agent-to-agent (A2A) connections, and memory hooks at deploy time, while the invoke request carries `model_id`, `connector_ids`, and credentials for run-time overrides.

## Credential Delegation Concern

Park surfaces an identity concern relevant to [[AI Agent Security]]. Capturing user credentials at the moment a user toggles on a connector imposes the **least consent fatigue**, because intentionality is highest at that point, and it avoids the failure mode of a long-running task pausing to request permission after the user has stepped away. He notes this single-hop credential capture is a *simplification* rather than a true solution to delegated authority; **RFC 8693 token exchange** (carrying an actor claim in the JWT) is the more complete mechanism. At the time of writing, AgentCore credential providers did not yet support per-user API keys, so per-user keys had to be injected via request headers instead.

## References
1. [Building an agent harness — Heeki Park (Medium)](https://heeki.medium.com/building-an-agent-harness-31942331d605)
2. [AWS Bedrock AgentCore harness documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/harness.html)

#### Tags
#harness_engineering #agentic_ai #ai_agents #aws #bedrock_agentcore #mcp #ai_agent_security
