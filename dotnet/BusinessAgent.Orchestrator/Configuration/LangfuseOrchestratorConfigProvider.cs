using System.Net.Http.Headers;
using System.Text;
using System.Text.Json;

namespace BusinessAgent.Orchestrator.Configuration;

public sealed class LangfuseOrchestratorConfigProvider(
    JsonOrchestratorConfigProvider fallbackProvider,
    IHttpClientFactory httpClientFactory,
    ILogger<LangfuseOrchestratorConfigProvider> logger) : IOrchestratorConfigProvider
{
    private const string DefaultPromptName = "Analyst Manager";
    private const string DefaultPromptLabel = "production";

    private OrchestratorConfig? _lastLoadedConfig;
    private string? _resolvedPath;

    public string ResolvedPath => _resolvedPath ?? fallbackProvider.ResolvedPath;

    public async Task<OrchestratorConfig> LoadAsync(CancellationToken cancellationToken = default)
    {
        if (ShouldUseLangfuse())
        {
            try
            {
                var langfuseConfig = await LoadFromLangfuseAsync(cancellationToken);
                _lastLoadedConfig = langfuseConfig;
                _resolvedPath = BuildResolvedPromptIdentifier();
                return langfuseConfig;
            }
            catch (Exception ex)
            {
                if (_lastLoadedConfig is not null)
                {
                    logger.LogWarning(
                        ex,
                        "Failed to load Langfuse prompt {PromptName}. Reusing the last applied configuration.",
                        GetPromptName());
                    return _lastLoadedConfig;
                }

                logger.LogWarning(
                    ex,
                    "Failed to load Langfuse prompt {PromptName}. Falling back to local JSON config.",
                    GetPromptName());
            }
        }

        var localConfig = await fallbackProvider.LoadAsync(cancellationToken);
        localConfig.Metadata.Source = "json";
        _lastLoadedConfig = localConfig;
        _resolvedPath = fallbackProvider.ResolvedPath;
        return localConfig;
    }

    private async Task<OrchestratorConfig> LoadFromLangfuseAsync(CancellationToken cancellationToken)
    {
        var publicKey = Environment.GetEnvironmentVariable("LANGFUSE_PUBLIC_KEY")
            ?? throw new InvalidOperationException("LANGFUSE_PUBLIC_KEY environment variable is required.");
        var secretKey = Environment.GetEnvironmentVariable("LANGFUSE_SECRET_KEY")
            ?? throw new InvalidOperationException("LANGFUSE_SECRET_KEY environment variable is required.");
        var baseUrl = GetBaseUrl();
        var promptName = GetPromptName();
        var promptLabel = GetPromptLabel();
        var promptVersion = GetPromptVersion();

        var requestUri = BuildPromptUri(baseUrl, promptName, promptLabel, promptVersion);
        using var request = new HttpRequestMessage(HttpMethod.Get, requestUri);

        var authBytes = Encoding.UTF8.GetBytes($"{publicKey}:{secretKey}");
        request.Headers.Authorization = new AuthenticationHeaderValue(
            "Basic",
            Convert.ToBase64String(authBytes));

        logger.LogInformation("Loading orchestrator prompt from Langfuse: {PromptUri}", requestUri);

        var client = httpClientFactory.CreateClient(nameof(LangfuseOrchestratorConfigProvider));
        using var response = await client.SendAsync(
            request,
            HttpCompletionOption.ResponseHeadersRead,
            cancellationToken);
        response.EnsureSuccessStatusCode();

        await using var responseStream = await response.Content.ReadAsStreamAsync(cancellationToken);
        using var document = await JsonDocument.ParseAsync(responseStream, cancellationToken: cancellationToken);

        var payload = document.RootElement;
        if (payload.ValueKind == JsonValueKind.Object
            && payload.TryGetProperty("data", out var dataElement)
            && dataElement.ValueKind == JsonValueKind.Object)
        {
            payload = dataElement;
        }

        var promptElement = payload.TryGetProperty("prompt", out var rawPromptElement)
            ? rawPromptElement
            : throw new InvalidOperationException(
                $"Langfuse prompt '{promptName}' did not include a prompt body.");

        var promptText = EnvironmentVariableExpander.Expand(RenderPrompt(promptElement));
        if (string.IsNullOrWhiteSpace(promptText))
        {
            throw new InvalidOperationException(
                $"Langfuse prompt '{promptName}' resolved to an empty prompt.");
        }

        var modelConfig = new OrchestratorModelConfig();
        if (payload.TryGetProperty("config", out var configElement)
            && configElement.ValueKind is not JsonValueKind.Null and not JsonValueKind.Undefined)
        {
            var expandedConfigJson = EnvironmentVariableExpander.Expand(configElement.GetRawText());
            modelConfig = JsonSerializer.Deserialize<OrchestratorModelConfig>(
                              expandedConfigJson,
                              JsonOptions()) ?? new OrchestratorModelConfig();
        }

        return new OrchestratorConfig
        {
            Prompt = promptText,
            Config = modelConfig,
            Metadata = new OrchestratorConfigMetadata
            {
                Source = "langfuse",
                PromptName = payload.TryGetProperty("name", out var nameElement)
                    ? nameElement.GetString() ?? promptName
                    : promptName,
                PromptVersion = payload.TryGetProperty("version", out var versionElement)
                    && versionElement.TryGetInt32(out var parsedVersion)
                        ? parsedVersion
                        : promptVersion,
                PromptLabel = promptVersion.HasValue ? null : promptLabel,
                PromptType = payload.TryGetProperty("type", out var typeElement)
                    ? typeElement.GetString()
                    : null,
            },
        };
    }

    private static Uri BuildPromptUri(
        string baseUrl,
        string promptName,
        string? promptLabel,
        int? promptVersion)
    {
        var builder = new StringBuilder();
        builder.Append(baseUrl.TrimEnd('/'));
        builder.Append("/api/public/v2/prompts/");
        builder.Append(Uri.EscapeDataString(promptName));

        if (promptVersion.HasValue)
        {
            builder.Append("?version=");
            builder.Append(promptVersion.Value);
        }
        else if (!string.IsNullOrWhiteSpace(promptLabel))
        {
            builder.Append("?label=");
            builder.Append(Uri.EscapeDataString(promptLabel));
        }

        return new Uri(builder.ToString(), UriKind.Absolute);
    }

    private static JsonSerializerOptions JsonOptions() =>
        new()
        {
            PropertyNameCaseInsensitive = true,
        };

    private static bool ShouldUseLangfuse()
    {
        var enabled = Environment.GetEnvironmentVariable("LANGFUSE_ENABLED");
        if (!string.IsNullOrWhiteSpace(enabled)
            && (enabled.Equals("false", StringComparison.OrdinalIgnoreCase)
                || enabled == "0"
                || enabled.Equals("no", StringComparison.OrdinalIgnoreCase)
                || enabled.Equals("off", StringComparison.OrdinalIgnoreCase)))
        {
            return false;
        }

        return !string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("LANGFUSE_PUBLIC_KEY"))
            && !string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("LANGFUSE_SECRET_KEY"));
    }

    private static string GetBaseUrl() =>
        Environment.GetEnvironmentVariable("LANGFUSE_BASE_URL")?.TrimEnd('/')
        ?? "https://cloud.langfuse.com";

    private static string GetPromptName() =>
        Environment.GetEnvironmentVariable("LANGFUSE_PROMPT_NAME")
        ?? Environment.GetEnvironmentVariable("AGENT_SETTINGS")
        ?? DefaultPromptName;

    private static string GetPromptLabel() =>
        Environment.GetEnvironmentVariable("LANGFUSE_PROMPT_LABEL")
        ?? DefaultPromptLabel;

    private static int? GetPromptVersion()
    {
        var rawVersion = Environment.GetEnvironmentVariable("LANGFUSE_PROMPT_VERSION");
        return int.TryParse(rawVersion, out var version)
            ? version
            : null;
    }

    private static string BuildResolvedPromptIdentifier()
    {
        var promptName = GetPromptName();
        var version = GetPromptVersion();
        var label = GetPromptLabel();
        var selector = version.HasValue
            ? $"version={version.Value}"
            : $"label={label}";
        return $"langfuse://{promptName}?{selector}";
    }

    private static string RenderPrompt(JsonElement promptElement) =>
        promptElement.ValueKind switch
        {
            JsonValueKind.String => promptElement.GetString() ?? string.Empty,
            JsonValueKind.Array => string.Join(
                Environment.NewLine + Environment.NewLine,
                promptElement.EnumerateArray()
                    .Select(RenderPromptMessage)
                    .Where(static value => !string.IsNullOrWhiteSpace(value))),
            JsonValueKind.Object => RenderPromptMessage(promptElement),
            JsonValueKind.Null or JsonValueKind.Undefined => string.Empty,
            _ => promptElement.GetRawText(),
        };

    private static string RenderPromptMessage(JsonElement promptMessage)
    {
        if (promptMessage.ValueKind == JsonValueKind.String)
        {
            return promptMessage.GetString() ?? string.Empty;
        }

        if (promptMessage.ValueKind != JsonValueKind.Object)
        {
            return promptMessage.GetRawText();
        }

        var role = promptMessage.TryGetProperty("role", out var roleElement)
            ? roleElement.GetString()
            : null;
        var content = promptMessage.TryGetProperty("content", out var contentElement)
            ? RenderPromptContent(contentElement)
            : promptMessage.GetRawText();

        if (string.IsNullOrWhiteSpace(role))
        {
            return content;
        }

        return $"{role}: {content}".Trim();
    }

    private static string RenderPromptContent(JsonElement contentElement) =>
        contentElement.ValueKind switch
        {
            JsonValueKind.String => contentElement.GetString() ?? string.Empty,
            JsonValueKind.Array => string.Join(
                Environment.NewLine,
                contentElement.EnumerateArray()
                    .Select(RenderPromptContentItem)
                    .Where(static value => !string.IsNullOrWhiteSpace(value))),
            JsonValueKind.Object => RenderPromptContentItem(contentElement),
            JsonValueKind.Null or JsonValueKind.Undefined => string.Empty,
            _ => contentElement.GetRawText(),
        };

    private static string RenderPromptContentItem(JsonElement itemElement)
    {
        if (itemElement.ValueKind == JsonValueKind.String)
        {
            return itemElement.GetString() ?? string.Empty;
        }

        if (itemElement.ValueKind == JsonValueKind.Object)
        {
            if (itemElement.TryGetProperty("text", out var textElement)
                && textElement.ValueKind == JsonValueKind.String)
            {
                return textElement.GetString() ?? string.Empty;
            }

            if (itemElement.TryGetProperty("content", out var nestedContent))
            {
                return RenderPromptContent(nestedContent);
            }
        }

        return itemElement.GetRawText();
    }
}
