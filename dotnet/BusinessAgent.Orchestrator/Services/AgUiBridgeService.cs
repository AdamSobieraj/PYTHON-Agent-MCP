using System.Runtime.CompilerServices;
using System.Text;
using System.Text.Json;
using System.Threading.Channels;

using A2A;

using BusinessAgent.Orchestrator.Models;

namespace BusinessAgent.Orchestrator.Services;

public sealed class AgUiBridgeService(
    string publicBaseUrl,
    AgUiThreadSessionStore sessionStore,
    ILogger<AgUiBridgeService> logger)
{
    private static readonly HashSet<string> s_pausedStates = new(
        ["input-required", "auth-required"],
        StringComparer.OrdinalIgnoreCase);

    private static readonly HashSet<string> s_terminalStates = new(
        ["completed", "failed", "rejected", "canceled"],
        StringComparer.OrdinalIgnoreCase);

    public IAsyncEnumerable<Dictionary<string, object?>> StreamEventsAsync(
        RunAgentInput input,
        CancellationToken cancellationToken = default)
    {
        var channel = Channel.CreateUnbounded<Dictionary<string, object?>>();

        _ = Task.Run(async () =>
        {
            try
            {
                await foreach (var payload in StreamEventsCoreAsync(input, cancellationToken))
                {
                    await channel.Writer.WriteAsync(payload, cancellationToken);
                }
            }
            catch (OperationCanceledException) when (cancellationToken.IsCancellationRequested)
            {
            }
            catch (Exception ex)
            {
                logger.LogError(ex, "AG-UI bridge failed for thread {ThreadId}", input.ThreadId);

                if (!cancellationToken.IsCancellationRequested)
                {
                    channel.Writer.TryWrite(Event(
                        "RUN_ERROR",
                        ("message", ex.Message),
                        ("code", "AGUI_BRIDGE_FAILED")));
                }
            }
            finally
            {
                channel.Writer.TryComplete();
            }
        }, CancellationToken.None);

        return channel.Reader.ReadAllAsync(cancellationToken);
    }

    private async IAsyncEnumerable<Dictionary<string, object?>> StreamEventsCoreAsync(
        RunAgentInput input,
        [EnumeratorCancellation] CancellationToken cancellationToken = default)
    {
        if (string.IsNullOrWhiteSpace(input.ThreadId))
        {
            throw new InvalidOperationException("AG-UI request must include threadId.");
        }

        if (string.IsNullOrWhiteSpace(input.RunId))
        {
            throw new InvalidOperationException("AG-UI request must include runId.");
        }

        var latestUserMessage = GetLatestUserMessage(input.Messages);
        if (latestUserMessage is null)
        {
            throw new InvalidOperationException("AG-UI request must contain at least one user message.");
        }

        var session = sessionStore.GetOrCreate(input.ThreadId);
        var activityMessageId = $"a2a-task-{input.ThreadId}";
        var assistantMessageId = $"assistant-{input.RunId}";
        var selfTargetUrl = $"{publicBaseUrl.TrimEnd('/')}/a2a/jsonrpc";

        if (!ShouldReuseTask(session))
        {
            session.LastStatusMessage = null;
        }

        session.TargetUrl = selfTargetUrl;
        session.Transport = "JSONRPC";

        yield return Event(
            "RUN_STARTED",
            ("threadId", input.ThreadId),
            ("runId", input.RunId));

        yield return ActivitySnapshotEvent(
            activityMessageId,
            BuildActivityContent(session, selfTargetUrl));
        yield return StateSnapshotEvent(BuildStateSnapshot(session, selfTargetUrl));

        var outboundText = BuildA2aRequestText(input, latestUserMessage, session);
        var a2aClient = new A2AClient(new Uri(selfTargetUrl));
        var request = new SendMessageRequest
        {
            Message = new Message
            {
                Role = Role.User,
                MessageId = string.IsNullOrWhiteSpace(latestUserMessage.Id)
                    ? Guid.NewGuid().ToString("N")
                    : latestUserMessage.Id,
                ContextId = session.ContextId ?? input.ThreadId,
                TaskId = ShouldReuseTask(session) ? session.TaskId : null,
                Parts = [Part.FromText(outboundText)],
            },
        };

        var emittedText = false;
        await foreach (var response in a2aClient.SendStreamingMessageAsync(request))
        {
            switch (response.PayloadCase)
            {
                case StreamResponseCase.StatusUpdate:
                    foreach (var statusEvent in ProcessStatusUpdate(
                                 response.StatusUpdate!,
                                 session,
                                 activityMessageId,
                                 assistantMessageId,
                                 selfTargetUrl))
                    {
                        if (statusEvent.TryGetValue("type", out var type)
                            && type?.ToString() == "TEXT_MESSAGE_CONTENT")
                        {
                            emittedText = true;
                        }

                        yield return statusEvent;
                    }

                    break;

                case StreamResponseCase.ArtifactUpdate:
                    foreach (var artifactEvent in ProcessArtifactUpdate(
                                 response.ArtifactUpdate!,
                                 session,
                                 activityMessageId,
                                 assistantMessageId,
                                 selfTargetUrl))
                    {
                        if (artifactEvent.TryGetValue("type", out var type)
                            && type?.ToString() == "TEXT_MESSAGE_CONTENT")
                        {
                            emittedText = true;
                        }

                        yield return artifactEvent;
                    }

                    break;

                case StreamResponseCase.Task:
                    foreach (var taskEvent in ProcessTask(
                                 response.Task!,
                                 session,
                                 activityMessageId,
                                 assistantMessageId,
                                 selfTargetUrl,
                                 emitTaskText: !emittedText))
                    {
                        yield return taskEvent;
                    }

                    break;

                case StreamResponseCase.Message:
                    foreach (var messageEvent in EmitAssistantText(
                                 assistantMessageId,
                                 OrchestratorRuntime.ExtractMessageText(response.Message)))
                    {
                        emittedText = true;
                        yield return messageEvent;
                    }

                    break;
            }
        }

        session.Initialized = true;
        yield return StateSnapshotEvent(BuildStateSnapshot(session, selfTargetUrl));

        if (session.LastTaskState is "failed" or "rejected" or "canceled")
        {
            yield return Event(
                "RUN_ERROR",
                ("message", session.LastStatusMessage ?? $"The A2A task ended with state '{session.LastTaskState}'."),
                ("code", session.LastTaskState));
            yield break;
        }

        yield return Event(
            "RUN_FINISHED",
            ("threadId", input.ThreadId),
            ("runId", input.RunId),
            ("result", new Dictionary<string, object?>
            {
                ["taskState"] = session.LastTaskState,
                ["contextId"] = session.ContextId,
                ["taskId"] = session.TaskId,
                ["target"] = new Dictionary<string, object?>
                {
                    ["url"] = session.TargetUrl ?? selfTargetUrl,
                    ["transport"] = session.Transport ?? "JSONRPC",
                },
            }));
    }

    private static bool ShouldReuseTask(AgUiThreadSession session) =>
        !string.IsNullOrWhiteSpace(session.TaskId)
        && !string.IsNullOrWhiteSpace(session.LastTaskState)
        && s_pausedStates.Contains(session.LastTaskState);

    private static IEnumerable<Dictionary<string, object?>> ProcessStatusUpdate(
        TaskStatusUpdateEvent statusUpdate,
        AgUiThreadSession session,
        string activityMessageId,
        string assistantMessageId,
        string targetUrl)
    {
        session.TaskId = statusUpdate.TaskId;
        session.ContextId = statusUpdate.ContextId;
        session.LastTaskState = OrchestratorRuntime.NormalizeTaskState(statusUpdate.Status.State);

        var statusText = OrchestratorRuntime.ExtractMessageText(statusUpdate.Status.Message);
        if (!string.IsNullOrWhiteSpace(statusText))
        {
            session.LastStatusMessage = statusText;
        }

        yield return ActivitySnapshotEvent(
            activityMessageId,
            BuildActivityContent(session, targetUrl));

        if ((session.LastTaskState is "input-required" or "auth-required" or "failed" or "rejected")
            && !string.IsNullOrWhiteSpace(statusText))
        {
            foreach (var textEvent in EmitAssistantText(assistantMessageId, statusText))
            {
                yield return textEvent;
            }
        }

        FinalizeSessionIfTerminal(session);
        yield return StateSnapshotEvent(BuildStateSnapshot(session, targetUrl));
    }

    private static IEnumerable<Dictionary<string, object?>> ProcessArtifactUpdate(
        TaskArtifactUpdateEvent artifactUpdate,
        AgUiThreadSession session,
        string activityMessageId,
        string assistantMessageId,
        string targetUrl)
    {
        session.TaskId = artifactUpdate.TaskId;
        session.ContextId = artifactUpdate.ContextId;

        yield return ActivitySnapshotEvent(
            activityMessageId,
            BuildActivityContent(session, targetUrl));

        var artifactText = OrchestratorRuntime.ExtractPartsText(artifactUpdate.Artifact.Parts);
        if (!string.IsNullOrWhiteSpace(artifactText))
        {
            foreach (var textEvent in EmitAssistantText(assistantMessageId, artifactText))
            {
                yield return textEvent;
            }
        }

        yield return StateSnapshotEvent(BuildStateSnapshot(session, targetUrl));
    }

    private static IEnumerable<Dictionary<string, object?>> ProcessTask(
        AgentTask task,
        AgUiThreadSession session,
        string activityMessageId,
        string assistantMessageId,
        string targetUrl,
        bool emitTaskText)
    {
        session.TaskId = task.Id;
        session.ContextId = task.ContextId;
        session.LastTaskState = OrchestratorRuntime.NormalizeTaskState(task.Status.State);

        var statusText = OrchestratorRuntime.ExtractMessageText(task.Status.Message);
        if (!string.IsNullOrWhiteSpace(statusText))
        {
            session.LastStatusMessage = statusText;
        }

        yield return ActivitySnapshotEvent(
            activityMessageId,
            BuildActivityContent(session, targetUrl));

        if (emitTaskText)
        {
            var artifactText = ExtractArtifactText(task.Artifacts);
            if (!string.IsNullOrWhiteSpace(artifactText))
            {
                foreach (var textEvent in EmitAssistantText(assistantMessageId, artifactText))
                {
                    yield return textEvent;
                }
            }
            else
            {
                if (!string.IsNullOrWhiteSpace(statusText))
                {
                    foreach (var textEvent in EmitAssistantText(assistantMessageId, statusText))
                    {
                        yield return textEvent;
                    }
                }
            }
        }

        FinalizeSessionIfTerminal(session);
        yield return StateSnapshotEvent(BuildStateSnapshot(session, targetUrl));
    }

    private static void FinalizeSessionIfTerminal(AgUiThreadSession session)
    {
        if (!string.IsNullOrWhiteSpace(session.LastTaskState)
            && s_terminalStates.Contains(session.LastTaskState)
            && !s_pausedStates.Contains(session.LastTaskState))
        {
            session.TaskId = null;
        }
    }

    private static string ExtractArtifactText(IEnumerable<Artifact>? artifacts)
    {
        if (artifacts is null)
        {
            return string.Empty;
        }

        var builder = new StringBuilder();
        foreach (var artifact in artifacts)
        {
            var text = OrchestratorRuntime.ExtractPartsText(artifact.Parts);
            if (string.IsNullOrWhiteSpace(text))
            {
                continue;
            }

            if (builder.Length > 0)
            {
                builder.AppendLine();
                builder.AppendLine();
            }

            builder.Append(text);
        }

        return builder.ToString().Trim();
    }

    private static AgUiMessage? GetLatestUserMessage(IEnumerable<AgUiMessage> messages) =>
        messages.LastOrDefault(message =>
            string.Equals(message.Role, "user", StringComparison.OrdinalIgnoreCase));

    private static string BuildA2aRequestText(
        RunAgentInput input,
        AgUiMessage latestUserMessage,
        AgUiThreadSession session)
    {
        var builder = new StringBuilder();

        if (!ShouldReuseTask(session))
        {
            var transcriptMessages = input.Messages
                .Where(message =>
                    !string.IsNullOrWhiteSpace(RenderContent(message.Content)))
                .ToList();

            if (transcriptMessages.Count > 1)
            {
                builder.AppendLine("Conversation transcript:");
                foreach (var message in transcriptMessages)
                {
                    builder.AppendLine(
                        $"- {message.Role}: {RenderContent(message.Content)}");
                }

                builder.AppendLine();
            }
        }

        builder.AppendLine(RenderContent(latestUserMessage.Content));

        if (input.Context.Count > 0)
        {
            builder.AppendLine();
            builder.AppendLine("Additional AG-UI context:");
            foreach (var contextItem in input.Context)
            {
                var value = RenderJsonValue(contextItem.Value);
                builder.AppendLine($"- {contextItem.Description}: {value}");
            }
        }

        return builder.ToString().Trim();
    }

    private static string RenderContent(JsonElement content)
    {
        return content.ValueKind switch
        {
            JsonValueKind.String => content.GetString() ?? string.Empty,
            JsonValueKind.Array => string.Join(
                Environment.NewLine,
                content.EnumerateArray()
                    .Select(RenderStructuredContentItem)
                    .Where(static item => !string.IsNullOrWhiteSpace(item))),
            JsonValueKind.Object => RenderStructuredContentItem(content),
            JsonValueKind.Undefined or JsonValueKind.Null => string.Empty,
            _ => content.GetRawText(),
        };
    }

    private static string RenderStructuredContentItem(JsonElement element)
    {
        if (element.ValueKind == JsonValueKind.String)
        {
            return element.GetString() ?? string.Empty;
        }

        if (element.ValueKind == JsonValueKind.Object)
        {
            if (element.TryGetProperty("text", out var textProperty)
                && textProperty.ValueKind == JsonValueKind.String)
            {
                return textProperty.GetString() ?? string.Empty;
            }

            if (element.TryGetProperty("type", out var typeProperty)
                && element.TryGetProperty("text", out textProperty)
                && typeProperty.ValueKind == JsonValueKind.String
                && string.Equals(typeProperty.GetString(), "text", StringComparison.OrdinalIgnoreCase)
                && textProperty.ValueKind == JsonValueKind.String)
            {
                return textProperty.GetString() ?? string.Empty;
            }

            return element.GetRawText();
        }

        return element.GetRawText();
    }

    private static string RenderJsonValue(JsonElement value) =>
        value.ValueKind switch
        {
            JsonValueKind.String => value.GetString() ?? string.Empty,
            JsonValueKind.Undefined or JsonValueKind.Null => string.Empty,
            _ => value.GetRawText(),
        };

    private static Dictionary<string, object?> BuildActivityContent(
        AgUiThreadSession session,
        string targetUrl) =>
        new()
        {
            ["taskId"] = session.TaskId,
            ["contextId"] = session.ContextId,
            ["taskState"] = session.LastTaskState,
            ["message"] = session.LastStatusMessage,
            ["url"] = session.TargetUrl ?? targetUrl,
            ["transport"] = session.Transport ?? "JSONRPC",
        };

    private static Dictionary<string, object?> BuildStateSnapshot(
        AgUiThreadSession session,
        string targetUrl) =>
        new()
        {
            ["a2a"] = new Dictionary<string, object?>
            {
                ["initialized"] = session.Initialized,
                ["url"] = session.TargetUrl ?? targetUrl,
                ["transport"] = session.Transport ?? "JSONRPC",
                ["contextId"] = session.ContextId,
                ["taskId"] = session.TaskId,
                ["taskState"] = session.LastTaskState,
            },
        };

    private static IEnumerable<Dictionary<string, object?>> EmitAssistantText(
        string messageId,
        string text)
    {
        if (string.IsNullOrWhiteSpace(text))
        {
            yield break;
        }

        yield return Event(
            "TEXT_MESSAGE_START",
            ("messageId", messageId),
            ("role", "assistant"));
        yield return Event(
            "TEXT_MESSAGE_CONTENT",
            ("messageId", messageId),
            ("delta", text));
        yield return Event(
            "TEXT_MESSAGE_END",
            ("messageId", messageId));
    }

    private static Dictionary<string, object?> ActivitySnapshotEvent(
        string messageId,
        Dictionary<string, object?> content) =>
        Event(
            "ACTIVITY_SNAPSHOT",
            ("messageId", messageId),
            ("activityType", "A2A_TASK"),
            ("content", content),
            ("replace", true));

    private static Dictionary<string, object?> StateSnapshotEvent(
        Dictionary<string, object?> snapshot) =>
        Event("STATE_SNAPSHOT", ("snapshot", snapshot));

    private static Dictionary<string, object?> Event(
        string eventType,
        params (string Key, object? Value)[] payload)
    {
        var data = new Dictionary<string, object?>
        {
            ["type"] = eventType,
        };

        foreach (var (key, value) in payload)
        {
            if (value is null)
            {
                continue;
            }

            data[key] = value;
        }

        return data;
    }
}

public sealed class AgUiEventEncoder
{
    private readonly bool _useSse;

    public AgUiEventEncoder(string? acceptHeader)
    {
        var normalizedAccept = (acceptHeader ?? string.Empty).ToLowerInvariant();
        _useSse = string.IsNullOrWhiteSpace(normalizedAccept)
            || normalizedAccept.Contains("text/event-stream", StringComparison.Ordinal)
            || normalizedAccept.Contains("*/*", StringComparison.Ordinal);
    }

    public string ContentType =>
        _useSse
            ? "text/event-stream"
            : "application/x-ndjson";

    public byte[] Encode(Dictionary<string, object?> payload)
    {
        var json = JsonSerializer.Serialize(payload);
        var body = _useSse
            ? $"data: {json}\n\n"
            : $"{json}\n";
        return Encoding.UTF8.GetBytes(body);
    }
}
