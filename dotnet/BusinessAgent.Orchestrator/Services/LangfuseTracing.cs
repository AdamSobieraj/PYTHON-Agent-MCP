using System.Diagnostics;
using System.Text;
using System.Text.Json;

using BusinessAgent.Orchestrator.Configuration;

using OpenTelemetry.Exporter;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;

namespace BusinessAgent.Orchestrator.Services;

internal static class LangfuseTracing
{
    public const string ActivitySourceName = "BusinessAgent.Orchestrator";

    public static readonly ActivitySource ActivitySource = new(ActivitySourceName);

    public static bool IsEnabled() =>
        !string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("LANGFUSE_PUBLIC_KEY"))
        && !string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("LANGFUSE_SECRET_KEY"))
        && !IsExplicitlyDisabled();

    public static void AddLangfuseOpenTelemetry(this IServiceCollection services)
    {
        if (!IsEnabled())
        {
            return;
        }

        var publicKey = Environment.GetEnvironmentVariable("LANGFUSE_PUBLIC_KEY")!;
        var secretKey = Environment.GetEnvironmentVariable("LANGFUSE_SECRET_KEY")!;
        var baseUrl = Environment.GetEnvironmentVariable("LANGFUSE_BASE_URL")?.TrimEnd('/')
            ?? "https://cloud.langfuse.com";
        var authHeader = Convert.ToBase64String(
            Encoding.UTF8.GetBytes($"{publicKey}:{secretKey}"));

        services.AddOpenTelemetry()
            .ConfigureResource(resource => resource.AddService(
                serviceName: "business-agent-orchestrator",
                serviceVersion: "1.0.0"))
            .WithTracing(tracing => tracing
                .AddSource(ActivitySourceName)
                .AddAspNetCoreInstrumentation()
                .AddHttpClientInstrumentation()
                .AddOtlpExporter(options =>
                {
                    // The .NET OTLP HTTP exporter expects the full signal-specific path.
                    options.Endpoint = new Uri($"{baseUrl}/api/public/otel/v1/traces");
                    options.Protocol = OtlpExportProtocol.HttpProtobuf;
                    options.Headers =
                        $"Authorization=Basic {authHeader},x-langfuse-ingestion-version=4";
                }));
    }

    public static Activity? StartAgentActivity(
        string activityName,
        string? input = null,
        string? sessionId = null,
        string? traceName = null,
        IReadOnlyDictionary<string, object?>? traceMetadata = null,
        IReadOnlyDictionary<string, object?>? observationMetadata = null)
        => StartObservationActivity(
            activityName,
            observationType: "agent",
            input,
            sessionId,
            traceName,
            traceMetadata,
            observationMetadata);

    public static Activity? StartChainActivity(
        string activityName,
        string? input = null,
        string? sessionId = null,
        string? traceName = null,
        IReadOnlyDictionary<string, object?>? traceMetadata = null,
        IReadOnlyDictionary<string, object?>? observationMetadata = null)
        => StartObservationActivity(
            activityName,
            observationType: "chain",
            input,
            sessionId,
            traceName,
            traceMetadata,
            observationMetadata);

    public static Activity? StartGenerationActivity(
        string activityName,
        string? input = null,
        string? model = null,
        OrchestratorConfig? runtimeConfig = null,
        IReadOnlyDictionary<string, object?>? observationMetadata = null)
    {
        var activity = StartObservationActivity(
            activityName,
            observationType: "generation",
            input,
            observationMetadata: observationMetadata);
        if (activity is null)
        {
            return null;
        }

        if (!string.IsNullOrWhiteSpace(input))
        {
            activity.SetTag("langfuse.observation.input", input);
        }

        if (!string.IsNullOrWhiteSpace(model))
        {
            activity.SetTag("langfuse.observation.model.name", model);
        }

        if (runtimeConfig?.Metadata is { Source: "langfuse", PromptName: not null } metadata)
        {
            activity.SetTag("langfuse.observation.prompt.name", metadata.PromptName);
            if (metadata.PromptVersion.HasValue)
            {
                activity.SetTag(
                    "langfuse.observation.prompt.version",
                    metadata.PromptVersion.Value);
            }
        }

        return activity;
    }

    public static Activity? StartToolActivity(
        string activityName,
        string? input = null,
        IReadOnlyDictionary<string, object?>? observationMetadata = null)
        => StartToolActivity(activityName, input, parentContext: null, observationMetadata);

    public static Activity? StartToolActivity(
        string activityName,
        string? input,
        ActivityContext? parentContext,
        IReadOnlyDictionary<string, object?>? observationMetadata = null)
        => StartObservationActivity(
            activityName,
            observationType: "tool",
            input,
            parentContext: parentContext,
            observationMetadata: observationMetadata);

    public static void SetModelParameters(Activity? activity, object? modelParameters)
    {
        if (activity is null || modelParameters is null)
        {
            return;
        }

        activity.SetTag(
            "langfuse.observation.model.parameters",
            JsonSerializer.Serialize(modelParameters));
    }

    public static void SetUsage(
        Activity? activity,
        IReadOnlyDictionary<string, object?>? usage)
    {
        if (activity is null || usage is null || usage.Count == 0)
        {
            return;
        }

        activity.SetTag(
            "langfuse.observation.usage_details",
            JsonSerializer.Serialize(usage));
    }

    public static void SetOutput(Activity? activity, string? output, bool traceLevel = false)
    {
        if (activity is null || string.IsNullOrWhiteSpace(output))
        {
            return;
        }

        activity.SetTag("langfuse.observation.output", output);
        if (traceLevel)
        {
            activity.SetTag("langfuse.trace.output", output);
        }
    }

    public static void MarkError(Activity? activity, Exception exception)
    {
        if (activity is null)
        {
            return;
        }

        activity.SetStatus(ActivityStatusCode.Error, exception.Message);
        activity.SetTag("langfuse.observation.level", "ERROR");
        activity.SetTag("langfuse.observation.status_message", exception.Message);
        activity.SetTag(
            "langfuse.observation.metadata.exception_type",
            exception.GetType().FullName);
    }

    private static void ApplyObservationDefaults(Activity activity, string observationType)
    {
        activity.SetTag("langfuse.observation.type", observationType);
        activity.SetTag("langfuse.observation.level", "DEFAULT");
        activity.SetTag("langfuse.environment", "default");
    }

    private static void ApplyTraceContext(
        Activity activity,
        string? input,
        string? sessionId,
        string? traceName,
        IReadOnlyDictionary<string, object?>? traceMetadata)
    {
        if (!string.IsNullOrWhiteSpace(input))
        {
            activity.SetTag("langfuse.observation.input", input);
            activity.SetTag("langfuse.trace.input", input);
        }

        if (!string.IsNullOrWhiteSpace(sessionId))
        {
            SetTraceContextAttribute(activity, "langfuse.session.id", sessionId);
        }

        if (!string.IsNullOrWhiteSpace(traceName))
        {
            SetTraceContextAttribute(activity, "langfuse.trace.name", traceName);
        }

        if (traceMetadata is null)
        {
            return;
        }

        foreach (var (key, value) in traceMetadata)
        {
            SetMetadataTag(activity, "langfuse.trace.metadata.", key, value);
        }
    }

    private static void ApplyObservationMetadata(
        Activity activity,
        IReadOnlyDictionary<string, object?>? observationMetadata)
    {
        if (observationMetadata is null)
        {
            return;
        }

        foreach (var (key, value) in observationMetadata)
        {
            SetMetadataTag(activity, "langfuse.observation.metadata.", key, value);
        }
    }

    private static void SetMetadataTag(
        Activity activity,
        string prefix,
        string key,
        object? value)
    {
        if (string.IsNullOrWhiteSpace(key) || value is null)
        {
            return;
        }

        var normalizedKey = key.Trim().Replace(' ', '_').Replace('-', '_');
        var serializedValue = value switch
        {
            string text => text,
            _ => JsonSerializer.Serialize(value),
        };
        var fullKey = $"{prefix}{normalizedKey}";
        activity.SetTag(fullKey, serializedValue);
        if (prefix.StartsWith("langfuse.trace.", StringComparison.Ordinal))
        {
            SetTraceContextBaggage(activity, fullKey, serializedValue);
        }
    }

    private static Activity? StartObservationActivity(
        string activityName,
        string observationType,
        string? input = null,
        string? sessionId = null,
        string? traceName = null,
        IReadOnlyDictionary<string, object?>? traceMetadata = null,
        IReadOnlyDictionary<string, object?>? observationMetadata = null,
        ActivityContext? parentContext = null)
    {
        var inheritedContext = CaptureInheritedTraceContext();
        var activity = parentContext.HasValue
            ? ActivitySource.StartActivity(activityName, ActivityKind.Internal, parentContext.Value)
            : ActivitySource.StartActivity(activityName, ActivityKind.Internal);
        if (activity is null)
        {
            return null;
        }

        ApplyObservationDefaults(activity, observationType);
        ApplyInheritedTraceContext(activity, inheritedContext);
        ApplyTraceContext(activity, input, sessionId, traceName, traceMetadata);
        ApplyObservationMetadata(activity, observationMetadata);
        return activity;
    }

    private static Dictionary<string, string> CaptureInheritedTraceContext()
    {
        var inherited = new Dictionary<string, string>(StringComparer.Ordinal);
        var currentActivity = Activity.Current;
        if (currentActivity is null)
        {
            return inherited;
        }

        foreach (var (key, value) in currentActivity.Baggage)
        {
            if (ShouldPropagateTraceContextKey(key) && !string.IsNullOrWhiteSpace(value))
            {
                inherited[key] = value;
            }
        }

        foreach (var (key, value) in currentActivity.Tags)
        {
            if (ShouldPropagateTraceContextKey(key)
                && !string.IsNullOrWhiteSpace(value)
                && !inherited.ContainsKey(key))
            {
                inherited[key] = value;
            }
        }

        return inherited;
    }

    private static void ApplyInheritedTraceContext(
        Activity activity,
        IReadOnlyDictionary<string, string> inheritedContext)
    {
        foreach (var (key, value) in inheritedContext)
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                continue;
            }

            activity.SetTag(key, value);
            SetTraceContextBaggage(activity, key, value);
        }
    }

    private static void SetTraceContextAttribute(Activity activity, string key, string value)
    {
        activity.SetTag(key, value);
        SetTraceContextBaggage(activity, key, value);
    }

    private static void SetTraceContextBaggage(Activity activity, string key, string value)
    {
        if (!ShouldPropagateTraceContextKey(key))
        {
            return;
        }

        activity.AddBaggage(key, value);
    }

    private static bool ShouldPropagateTraceContextKey(string key) =>
        key is "langfuse.session.id"
            or "langfuse.user.id"
            or "langfuse.trace.name"
            or "langfuse.trace.tags"
            or "langfuse.version"
            or "langfuse.release"
        || key.StartsWith("langfuse.trace.metadata.", StringComparison.Ordinal);

    private static bool IsExplicitlyDisabled()
    {
        var rawValue = Environment.GetEnvironmentVariable("LANGFUSE_ENABLED");
        return !string.IsNullOrWhiteSpace(rawValue)
            && (rawValue.Equals("false", StringComparison.OrdinalIgnoreCase)
                || rawValue == "0"
                || rawValue.Equals("no", StringComparison.OrdinalIgnoreCase)
                || rawValue.Equals("off", StringComparison.OrdinalIgnoreCase));
    }
}
