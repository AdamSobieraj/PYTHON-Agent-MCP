namespace BusinessAgent.Orchestrator.Models;

public sealed class DiscoverySnapshot
{
    public DateTimeOffset LoadedAt { get; init; }

    public string ConfigPath { get; init; } = string.Empty;

    public string ConfigSource { get; init; } = "json";

    public string? PromptName { get; init; }

    public int? PromptVersion { get; init; }

    public string? PromptLabel { get; init; }

    public IReadOnlyList<DiscoveredA2AAgent> A2aAgents { get; init; } =
        Array.Empty<DiscoveredA2AAgent>();

    public IReadOnlyList<DiscoveredMcpTool> McpTools { get; init; } =
        Array.Empty<DiscoveredMcpTool>();

    public IReadOnlyList<string> Warnings { get; init; } = Array.Empty<string>();
}

public sealed record DiscoveredA2AAgent(
    string Name,
    string DisplayName,
    string Description,
    string EndpointUrl,
    string ProtocolBinding,
    IReadOnlyList<string> Skills);

public sealed record DiscoveredMcpTool(
    string ServerName,
    string ToolName,
    string Description);
