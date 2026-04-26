using A2A;

namespace BusinessAgent.Orchestrator.Configuration;

internal static class AgentCardFactory
{
    public static AgentCard Build(string publicBaseUrl, OrchestratorConfig? runtimeConfig = null)
    {
        var agentCardConfig = runtimeConfig?.Config.AgentCard;
        var inputModes = agentCardConfig?.DefaultInputModes is { Count: > 0 }
            ? new List<string>(agentCardConfig.DefaultInputModes)
            : new List<string> { "text" };
        var outputModes = agentCardConfig?.DefaultOutputModes is { Count: > 0 }
            ? new List<string>(agentCardConfig.DefaultOutputModes)
            : new List<string> { "text", "task-status" };

        var capabilities = new AgentCapabilities
        {
            Streaming = agentCardConfig?.Capabilities?.Streaming ?? true,
            PushNotifications = agentCardConfig?.Capabilities?.PushNotifications ?? false,
        };

        var skills = agentCardConfig?.Skills is { Count: > 0 }
            ? agentCardConfig.Skills.Select(skill => new AgentSkill
                {
                    Id = skill.Id,
                    Name = skill.Name,
                    Description = skill.Description,
                    Tags = [.. skill.Tags],
                    Examples = [.. (skill.Examples ?? [])],
                    InputModes = [.. (skill.InputModes ?? inputModes)],
                    OutputModes = [.. (skill.OutputModes ?? outputModes)],
                })
                .ToList()
            : new List<AgentSkill>
            {
                new()
                {
                    Id = "business_orchestration",
                    Name = "Business Orchestration",
                    Description =
                        "Routes work across discovered MCP tools and discovered A2A agents.",
                    Tags = ["orchestrator", "a2a", "mcp", "semantic-kernel"],
                    Examples =
                    [
                        "Use the knowledge base and then delegate deeper analysis to the research agent.",
                        "Coordinate an answer that combines MCP retrieval and another specialist A2A agent.",
                    ],
                    InputModes = inputModes,
                    OutputModes = outputModes,
                },
            };

        var providerUrl = agentCardConfig?.Provider?.Url;
        if (string.IsNullOrWhiteSpace(providerUrl))
        {
            providerUrl = publicBaseUrl;
        }

        return new AgentCard
        {
            Name = agentCardConfig?.Name ?? "Business Agent Orchestrator",
            Description = agentCardConfig?.Description
                ?? "Coordinates discovered MCP tools and discovered A2A agents for user requests.",
            Provider = new AgentProvider
            {
                Organization = agentCardConfig?.Provider?.Organization ?? "Business Agent",
                Url = providerUrl,
            },
            Version = agentCardConfig?.Version ?? "1.0.0",
            DefaultInputModes = inputModes,
            DefaultOutputModes = outputModes,
            Capabilities = capabilities,
            SupportedInterfaces =
            [
                new AgentInterface
                {
                    Url = $"{publicBaseUrl}/a2a/jsonrpc",
                    ProtocolBinding = "JSONRPC",
                    ProtocolVersion = "1.0",
                },
                new AgentInterface
                {
                    Url = $"{publicBaseUrl}/a2a/rest",
                    ProtocolBinding = "HTTP+JSON",
                    ProtocolVersion = "1.0",
                },
            ],
            Skills = skills,
        };
    }

    public static void ApplyTo(
        AgentCard target,
        string publicBaseUrl,
        OrchestratorConfig runtimeConfig)
    {
        var rebuilt = Build(publicBaseUrl, runtimeConfig);
        target.Name = rebuilt.Name;
        target.Description = rebuilt.Description;
        target.Provider = rebuilt.Provider;
        target.Version = rebuilt.Version;
        target.DefaultInputModes = rebuilt.DefaultInputModes;
        target.DefaultOutputModes = rebuilt.DefaultOutputModes;
        target.Capabilities = rebuilt.Capabilities;
        target.SupportedInterfaces = rebuilt.SupportedInterfaces;
        target.Skills = rebuilt.Skills;
    }
}
