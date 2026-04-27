using System.Text.Json.Serialization;

namespace BusinessAgent.Orchestrator.Configuration;

public sealed class OrchestratorConfig
{
    [JsonPropertyName("prompt")]
    public string Prompt { get; set; } = string.Empty;

    [JsonPropertyName("config")]
    public OrchestratorModelConfig Config { get; set; } = new();

    [JsonIgnore]
    public OrchestratorConfigMetadata Metadata { get; set; } = new();
}

public sealed class OrchestratorConfigMetadata
{
    public string Source { get; set; } = "json";

    public string? PromptName { get; set; }

    public int? PromptVersion { get; set; }

    public string? PromptLabel { get; set; }

    public string? PromptType { get; set; }
}

public sealed class OrchestratorModelConfig
{
    [JsonPropertyName("temperature")]
    public double Temperature { get; set; }

    [JsonPropertyName("agent_card")]
    public AgentCardConfig? AgentCard { get; set; }

    [JsonPropertyName("agentCard")]
    public AgentCardConfig? AgentCardAlias
    {
        get => this.AgentCard;
        set => this.AgentCard = value;
    }

    [JsonPropertyName("mcp_servers")]
    public List<McpServerConfig> McpServers { get; set; } = [];

    [JsonPropertyName("mcpServers")]
    public List<McpServerConfig>? McpServersAlias
    {
        get => this.McpServers;
        set => this.McpServers = value ?? [];
    }

    [JsonPropertyName("a2a_agents")]
    public List<A2AAgentConfig> A2aAgents { get; set; } = [];

    [JsonPropertyName("a2aAgents")]
    public List<A2AAgentConfig>? A2aAgentsAlias
    {
        get => this.A2aAgents;
        set => this.A2aAgents = value ?? [];
    }
}

public sealed class AgentCardConfig
{
    [JsonPropertyName("name")]
    public string? Name { get; set; }

    [JsonPropertyName("description")]
    public string? Description { get; set; }

    [JsonPropertyName("version")]
    public string? Version { get; set; }

    [JsonPropertyName("provider")]
    public AgentCardProviderConfig? Provider { get; set; }

    [JsonPropertyName("capabilities")]
    public AgentCardCapabilitiesConfig? Capabilities { get; set; }

    [JsonPropertyName("default_input_modes")]
    public List<string>? DefaultInputModes { get; set; }

    [JsonPropertyName("defaultInputModes")]
    public List<string>? DefaultInputModesAlias
    {
        get => this.DefaultInputModes;
        set => this.DefaultInputModes = value;
    }

    [JsonPropertyName("default_output_modes")]
    public List<string>? DefaultOutputModes { get; set; }

    [JsonPropertyName("defaultOutputModes")]
    public List<string>? DefaultOutputModesAlias
    {
        get => this.DefaultOutputModes;
        set => this.DefaultOutputModes = value;
    }

    [JsonPropertyName("skills")]
    public List<AgentCardSkillConfig>? Skills { get; set; }
}

public sealed class AgentCardProviderConfig
{
    [JsonPropertyName("organization")]
    public string? Organization { get; set; }

    [JsonPropertyName("url")]
    public string? Url { get; set; }
}

public sealed class AgentCardCapabilitiesConfig
{
    [JsonPropertyName("streaming")]
    public bool? Streaming { get; set; }

    [JsonPropertyName("push_notifications")]
    public bool? PushNotifications { get; set; }

    [JsonPropertyName("pushNotifications")]
    public bool? PushNotificationsAlias
    {
        get => this.PushNotifications;
        set => this.PushNotifications = value;
    }
}

public sealed class AgentCardSkillConfig
{
    [JsonPropertyName("id")]
    public string Id { get; set; } = string.Empty;

    [JsonPropertyName("name")]
    public string Name { get; set; } = string.Empty;

    [JsonPropertyName("description")]
    public string Description { get; set; } = string.Empty;

    [JsonPropertyName("tags")]
    public List<string> Tags { get; set; } = [];

    [JsonPropertyName("examples")]
    public List<string>? Examples { get; set; }

    [JsonPropertyName("input_modes")]
    public List<string>? InputModes { get; set; }

    [JsonPropertyName("inputModes")]
    public List<string>? InputModesAlias
    {
        get => this.InputModes;
        set => this.InputModes = value;
    }

    [JsonPropertyName("output_modes")]
    public List<string>? OutputModes { get; set; }

    [JsonPropertyName("outputModes")]
    public List<string>? OutputModesAlias
    {
        get => this.OutputModes;
        set => this.OutputModes = value;
    }
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

    [JsonPropertyName("toolNamePrefix")]
    public string? ToolNamePrefixAlias
    {
        get => this.ToolNamePrefix;
        set => this.ToolNamePrefix = value;
    }

    [JsonPropertyName("allowed_tools")]
    public List<string> AllowedTools { get; set; } = [];

    [JsonPropertyName("allowedTools")]
    public List<string>? AllowedToolsAlias
    {
        get => this.AllowedTools;
        set => this.AllowedTools = value ?? [];
    }

    [JsonPropertyName("blocked_tools")]
    public List<string> BlockedTools { get; set; } = [];

    [JsonPropertyName("blockedTools")]
    public List<string>? BlockedToolsAlias
    {
        get => this.BlockedTools;
        set => this.BlockedTools = value ?? [];
    }

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
