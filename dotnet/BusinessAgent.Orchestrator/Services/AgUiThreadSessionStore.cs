using System.Collections.Concurrent;

namespace BusinessAgent.Orchestrator.Services;

public sealed class AgUiThreadSession
{
    public required string ThreadId { get; init; }

    public bool Initialized { get; set; }

    public string? TaskId { get; set; }

    public string? ContextId { get; set; }

    public string? LastTaskState { get; set; }

    public string? LastStatusMessage { get; set; }

    public string? TargetUrl { get; set; }

    public string? Transport { get; set; }
}

public sealed class AgUiThreadSessionStore
{
    private readonly ConcurrentDictionary<string, AgUiThreadSession> _sessions =
        new(StringComparer.OrdinalIgnoreCase);

    public AgUiThreadSession GetOrCreate(string threadId) =>
        _sessions.GetOrAdd(
            threadId,
            static id => new AgUiThreadSession
            {
                ThreadId = id,
            });
}
