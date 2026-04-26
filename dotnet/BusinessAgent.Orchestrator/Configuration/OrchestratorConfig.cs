using System.Text.Json.Serialization;

namespace BusinessAgent.Orchestrator.Configuration;

public sealed class OrchestratorConfig
{
    [JsonPropertyName("prompt")]
    public string Prompt { get; set; } = string.Empty;

    [JsonPropertyName("config")]
    public OrchestratorModelConfig Config { get; set; } = new();
}

public sealed class OrchestratorModelConfig
{
    [JsonPropertyName("temperature")]
    public double Temperature { get; set; }

    [JsonPropertyName("mcp_servers")]
    public List<McpServerConfig> McpServers { get; set; } = [];

    [JsonPropertyName("a2a_agents")]
    public List<A2AAgentConfig> A2aAgents { get; set; } = [];
}

public sealed class McpServerConfig
{
    [JsonPropertyName("name")]
    public string? Name { get; set; }

    [JsonPropertyName("enabled")]
    public bool Enabled { get; set; } = true;

    [JsonPropertyName("transport")]
    public string Transport { get; set; } = "streamable_http";

    [JsonPropertyName("url")]
    public string? Url { get; set; }

    [JsonPropertyName("tool_name_prefix")]
    public string? ToolNamePrefix { get; set; }

    [JsonPropertyName("allowed_tools")]
    public List<string> AllowedTools { get; set; } = [];

    [JsonPropertyName("blocked_tools")]
    public List<string> BlockedTools { get; set; } = [];

    [JsonPropertyName("headers")]
    public Dictionary<string, string>? Headers { get; set; }

    public string ResolvedName() =>
        string.IsNullOrWhiteSpace(this.Name)
            ? this.Url ?? "mcp_server"
            : this.Name;
}

public sealed class A2AAgentConfig
{
    [JsonPropertyName("name")]
    public string? Name { get; set; }

    [JsonPropertyName("enabled")]
    public bool Enabled { get; set; } = true;

    [JsonPropertyName("url")]
    public string Url { get; set; } = string.Empty;

    [JsonPropertyName("transport")]
    public string? Transport { get; set; }

    public string ResolvedName() =>
        string.IsNullOrWhiteSpace(this.Name)
            ? this.Url
            : this.Name;
}
