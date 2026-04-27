using System.Text.Json;
using System.Text.Json.Serialization;

namespace BusinessAgent.Orchestrator.Models;

public sealed class RunAgentInput
{
    [JsonPropertyName("threadId")]
    public string ThreadId { get; set; } = string.Empty;

    [JsonPropertyName("runId")]
    public string RunId { get; set; } = string.Empty;

    [JsonPropertyName("parentRunId")]
    public string? ParentRunId { get; set; }

    [JsonPropertyName("state")]
    public JsonElement State { get; set; }

    [JsonPropertyName("messages")]
    public List<AgUiMessage> Messages { get; set; } = [];

    [JsonPropertyName("context")]
    public List<AgUiContext> Context { get; set; } = [];

    [JsonPropertyName("forwardedProps")]
    public JsonElement ForwardedProps { get; set; }
}

public sealed class AgUiMessage
{
    [JsonPropertyName("id")]
    public string Id { get; set; } = string.Empty;

    [JsonPropertyName("role")]
    public string Role { get; set; } = string.Empty;

    [JsonPropertyName("content")]
    public JsonElement Content { get; set; }
}

public sealed class AgUiContext
{
    [JsonPropertyName("description")]
    public string Description { get; set; } = string.Empty;

    [JsonPropertyName("value")]
    public JsonElement Value { get; set; }
}
