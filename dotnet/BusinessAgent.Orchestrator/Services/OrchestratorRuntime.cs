using System.Diagnostics;
using System.Text;
using System.Text.Json;

using A2A;

using BusinessAgent.Orchestrator.Configuration;
using BusinessAgent.Orchestrator.Models;

using Microsoft.Extensions.DependencyInjection;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;

using ModelContextProtocol.Client;

namespace BusinessAgent.Orchestrator.Services;

public sealed class OrchestratorRuntime(
    IOrchestratorConfigProvider configProvider,
    ILoggerFactory loggerFactory) : IAsyncDisposable
{
    private const string RawChatCompletionServiceId = "orchestrator-openai-raw";

    private readonly SemaphoreSlim _initializeLock = new(1, 1);
    private readonly List<IAsyncDisposable> _asyncDisposables = [];
    private readonly Dictionary<string, DiscoveredA2AAgent> _a2aAgents =
        new(StringComparer.OrdinalIgnoreCase);
    private readonly ILogger<OrchestratorRuntime> _logger =
        loggerFactory.CreateLogger<OrchestratorRuntime>();

    private bool _initialized;
    private ChatCompletionAgent? _agent;

    public OrchestratorConfig RuntimeConfig { get; private set; } = new();

    public DiscoverySnapshot Snapshot { get; private set; } = new();

    public async Task InitializeAsync(CancellationToken cancellationToken = default)
    {
        if (_initialized)
        {
            return;
        }

        await _initializeLock.WaitAsync(cancellationToken);
        Activity? initializeActivity = null;
        try
        {
            if (_initialized)
            {
                return;
            }

            RuntimeConfig = await configProvider.LoadAsync(cancellationToken);
            initializeActivity = LangfuseTracing.StartAgentActivity(
                "orchestrator.initialize",
                traceName: "orchestrator-startup",
                traceMetadata: new Dictionary<string, object?>
                {
                    ["config_source"] = RuntimeConfig.Metadata.Source,
                    ["config_reference"] = configProvider.ResolvedPath,
                });
            ValidateChatConfiguration();

            var discoveryWarnings = new List<string>();
            var discoveredMcpTools = new List<DiscoveredMcpTool>();
            var discoveredA2aAgents = new List<DiscoveredA2AAgent>();

            var kernelBuilder = Kernel.CreateBuilder();
            ConfigureChatCompletion(kernelBuilder, RuntimeConfig);

            var delegationLogger = loggerFactory.CreateLogger<A2ADelegationPlugin>();
            kernelBuilder.Plugins.AddFromObject(
                new A2ADelegationPlugin(this, delegationLogger));

            foreach (var agentConfig in RuntimeConfig.Config.A2aAgents.Where(static agent => agent.Enabled))
            {
                try
                {
                    var discoveredAgent = await DiscoverA2aAgentAsync(agentConfig);
                    _a2aAgents[discoveredAgent.Name] = discoveredAgent;
                    discoveredA2aAgents.Add(discoveredAgent);
                }
                catch (Exception ex)
                {
                    var warning =
                        $"Failed to discover A2A agent '{agentConfig.ResolvedName()}': {ex.Message}";
                    _logger.LogWarning(ex, warning);
                    discoveryWarnings.Add(warning);
                }
            }

            var kernel = kernelBuilder.Build();

            foreach (var serverConfig in RuntimeConfig.Config.McpServers.Where(static server => server.Enabled))
            {
                try
                {
                    var serverTools = await DiscoverMcpToolsAsync(
                        kernel,
                        serverConfig,
                        cancellationToken);
                    discoveredMcpTools.AddRange(serverTools);
                }
                catch (Exception ex)
                {
                    var warning =
                        $"Failed to discover MCP server '{serverConfig.ResolvedName()}': {ex.Message}";
                    _logger.LogWarning(ex, warning);
                    discoveryWarnings.Add(warning);
                }
            }

            _agent = new ChatCompletionAgent
            {
                Name = "BusinessAgentOrchestrator",
                Instructions = BuildAgentInstructions(
                    RuntimeConfig,
                    discoveredA2aAgents,
                    discoveredMcpTools),
                Kernel = kernel,
                Arguments = new KernelArguments(
                    new OpenAIPromptExecutionSettings
                    {
                        Temperature = RuntimeConfig.Config.Temperature,
                        FunctionChoiceBehavior = FunctionChoiceBehavior.Auto(),
                    }),
            };

            Snapshot = new DiscoverySnapshot
            {
                LoadedAt = DateTimeOffset.UtcNow,
                ConfigPath = configProvider.ResolvedPath,
                ConfigSource = RuntimeConfig.Metadata.Source,
                PromptName = RuntimeConfig.Metadata.PromptName,
                PromptVersion = RuntimeConfig.Metadata.PromptVersion,
                PromptLabel = RuntimeConfig.Metadata.PromptLabel,
                A2aAgents = discoveredA2aAgents,
                McpTools = discoveredMcpTools,
                Warnings = discoveryWarnings,
            };

            _logger.LogInformation(
                "Orchestrator initialized. Discovered {AgentCount} A2A agents and {ToolCount} MCP tools.",
                discoveredA2aAgents.Count,
                discoveredMcpTools.Count);

            LangfuseTracing.SetOutput(
                initializeActivity,
                JsonSerializer.Serialize(new
                {
                    a2aAgents = discoveredA2aAgents.Count,
                    mcpTools = discoveredMcpTools.Count,
                    warnings = discoveryWarnings.Count,
                }),
                traceLevel: true);
            _initialized = true;
        }
        catch (Exception ex)
        {
            LangfuseTracing.MarkError(initializeActivity, ex);
            throw;
        }
        finally
        {
            initializeActivity?.Dispose();
            _initializeLock.Release();
        }
    }

    public IEnumerable<string> GetKnownA2aAgentNames() => _a2aAgents.Keys.OrderBy(static key => key);

    public DiscoveredA2AAgent? TryGetA2aAgent(string agentName)
    {
        _a2aAgents.TryGetValue(agentName, out var agent);
        return agent;
    }

    public async Task<string> GenerateResponseAsync(
        string requestText,
        CancellationToken cancellationToken = default)
    {
        await InitializeAsync(cancellationToken);

        if (_agent is null)
        {
            throw new InvalidOperationException("The orchestrator agent has not been initialized.");
        }

        Activity? chainActivity = null;
        var responseBuilder = new StringBuilder();
        try
        {
            chainActivity = LangfuseTracing.StartChainActivity(
                "orchestrator.semantic_kernel_run",
                input: requestText,
                traceName: "business-agent-orchestrator-run",
                sessionId: Activity.Current?.GetBaggageItem("langfuse.session.id"),
                traceMetadata: new Dictionary<string, object?>
                {
                    ["config_source"] = RuntimeConfig.Metadata.Source,
                    ["config_reference"] = configProvider.ResolvedPath,
                },
                observationMetadata: new Dictionary<string, object?>
                {
                    ["config_source"] = RuntimeConfig.Metadata.Source,
                    ["config_reference"] = configProvider.ResolvedPath,
                    ["execution_engine"] = "semantic-kernel",
                });

            await foreach (AgentResponseItem<ChatMessageContent> response in _agent.InvokeAsync(
                requestText,
                cancellationToken: cancellationToken))
            {
                if (!string.IsNullOrWhiteSpace(response.Message.Content))
                {
                    responseBuilder.Append(response.Message.Content);
                }
            }

            var finalText = responseBuilder.ToString().Trim();
            LangfuseTracing.SetOutput(chainActivity, finalText);
            return finalText;
        }
        catch (Exception ex)
        {
            LangfuseTracing.MarkError(chainActivity, ex);
            throw;
        }
        finally
        {
            chainActivity?.Dispose();
        }
    }

    public string FormatDelegatedResponse(
        DiscoveredA2AAgent agent,
        SendMessageResponse response)
    {
        if (response.Message is not null)
        {
            return FormatMessageParts(agent.DisplayName, response.Message.Parts);
        }

        if (response.Task is not null)
        {
            var artifactText = ExtractArtifactsText(response.Task.Artifacts);
            if (!string.IsNullOrWhiteSpace(artifactText))
            {
                return artifactText;
            }

            var statusText = ExtractMessageText(response.Task.Status.Message);
            if (!string.IsNullOrWhiteSpace(statusText))
            {
                return statusText;
            }

            return
                $"{agent.DisplayName} returned task state '{NormalizeTaskState(response.Task.Status.State)}' without text output.";
        }

        return $"{agent.DisplayName} returned an empty A2A response.";
    }

    public async ValueTask DisposeAsync()
    {
        for (var index = _asyncDisposables.Count - 1; index >= 0; index--)
        {
            try
            {
                await _asyncDisposables[index].DisposeAsync();
            }
            catch (Exception ex)
            {
                _logger.LogDebug(ex, "Async disposal failed while shutting down orchestrator runtime.");
            }
        }

        _initializeLock.Dispose();
    }

    private static void ValidateChatConfiguration()
    {
        if (string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("CHAT_BASE_URL")))
        {
            throw new InvalidOperationException("CHAT_BASE_URL environment variable is required.");
        }

        if (string.IsNullOrWhiteSpace(Environment.GetEnvironmentVariable("CHAT_MODEL")))
        {
            throw new InvalidOperationException("CHAT_MODEL environment variable is required.");
        }
    }

    private static void ConfigureChatCompletion(
        IKernelBuilder kernelBuilder,
        OrchestratorConfig runtimeConfig)
    {
        var modelId = Environment.GetEnvironmentVariable("CHAT_MODEL")
            ?? throw new InvalidOperationException("CHAT_MODEL environment variable is required.");
        var endpoint = Environment.GetEnvironmentVariable("CHAT_BASE_URL")
            ?? throw new InvalidOperationException("CHAT_BASE_URL environment variable is required.");
        var apiKey = Environment.GetEnvironmentVariable("CHAT_API_KEY") ?? "EMPTY";

        kernelBuilder.AddOpenAIChatCompletion(
            modelId: modelId,
            endpoint: new Uri(endpoint),
            apiKey: apiKey,
            orgId: null,
            serviceId: RawChatCompletionServiceId);
        kernelBuilder.Services.AddSingleton<IChatCompletionService>(serviceProvider =>
            new TracedChatCompletionService(
                serviceProvider.GetRequiredKeyedService<IChatCompletionService>(RawChatCompletionServiceId),
                runtimeConfig,
                modelId));
    }

    private async Task<DiscoveredA2AAgent> DiscoverA2aAgentAsync(A2AAgentConfig agentConfig)
    {
        var discoveryActivity = LangfuseTracing.StartToolActivity(
            "orchestrator.discover_a2a_agent",
            observationMetadata: new Dictionary<string, object?>
            {
                ["agent_name"] = agentConfig.ResolvedName(),
                ["agent_url"] = agentConfig.Url,
            });

        try
        {
        EnsureResolvedEndpoint(agentConfig.Url, $"A2A agent '{agentConfig.ResolvedName()}'");

        var resolver = new A2ACardResolver(new Uri(agentConfig.Url));
        var card = await resolver.GetAgentCardAsync();
        var selectedInterface = ChooseA2aInterface(card, agentConfig.Transport)
            ?? throw new InvalidOperationException(
                $"No suitable 1.0 interface was found for '{agentConfig.Url}'.");

        var discoveredName = NormalizeIdentifier(agentConfig.ResolvedName());
        var skillDescriptions = (card.Skills ?? [])
            .Select(skill => string.IsNullOrWhiteSpace(skill.Description)
                ? skill.Name
                : $"{skill.Name}: {skill.Description}")
            .ToList();

        return new DiscoveredA2AAgent(
            Name: discoveredName,
            DisplayName: card.Name,
            Description: card.Description,
            EndpointUrl: selectedInterface.Url,
            ProtocolBinding: selectedInterface.ProtocolBinding,
            Skills: skillDescriptions);
        }
        catch (Exception ex)
        {
            LangfuseTracing.MarkError(discoveryActivity, ex);
            throw;
        }
        finally
        {
            discoveryActivity?.Dispose();
        }
    }

    private async Task<IReadOnlyList<DiscoveredMcpTool>> DiscoverMcpToolsAsync(
        Kernel kernel,
        McpServerConfig serverConfig,
        CancellationToken cancellationToken)
    {
        var discoveryActivity = LangfuseTracing.StartToolActivity(
            "orchestrator.discover_mcp_tools",
            observationMetadata: new Dictionary<string, object?>
            {
                ["server_name"] = serverConfig.ResolvedName(),
                ["transport"] = serverConfig.Transport,
                ["endpoint"] = serverConfig.Url,
            });

        try
        {
        var normalizedTransport = NormalizeIdentifier(serverConfig.Transport);
        if (normalizedTransport is not ("streamable_http" or "streamablehttp"))
        {
            throw new NotSupportedException(
                $"MCP transport '{serverConfig.Transport}' is not supported by this basic orchestrator yet.");
        }

        if (string.IsNullOrWhiteSpace(serverConfig.Url))
        {
            throw new InvalidOperationException(
                $"MCP server '{serverConfig.ResolvedName()}' requires a url.");
        }

        EnsureResolvedEndpoint(serverConfig.Url, $"MCP server '{serverConfig.ResolvedName()}'");

        var serverName = NormalizeIdentifier(serverConfig.ResolvedName());
        var transport = new HttpClientTransport(
            new()
            {
                Endpoint = new Uri(serverConfig.Url),
                Name = serverName,
                TransportMode = HttpTransportMode.StreamableHttp,
                AdditionalHeaders = serverConfig.Headers is { Count: > 0 }
                    ? new Dictionary<string, string>(serverConfig.Headers)
                    : null,
            },
            loggerFactory);
        _asyncDisposables.Add(transport);

        var mcpClient = await McpClient.CreateAsync(
            transport,
            loggerFactory: loggerFactory,
            cancellationToken: cancellationToken);
        _asyncDisposables.Add(mcpClient);

        var rawTools = await mcpClient.ListToolsAsync().ConfigureAwait(false);
        var usableTools = rawTools
            .Where(tool => MatchesToolFilters(tool.Name, serverConfig))
            .ToList();

        if (usableTools.Count == 0)
        {
            _logger.LogInformation(
                "MCP server {ServerName} exposed no usable tools after applying filters.",
                serverName);
            return Array.Empty<DiscoveredMcpTool>();
        }

        kernel.Plugins.AddFromFunctions(
            serverName,
            usableTools.Select(tool => tool.AsKernelFunction()));

        return usableTools
            .Select(tool => new DiscoveredMcpTool(
                ServerName: serverName,
                ToolName: tool.Name,
                Description: tool.Description ?? string.Empty))
            .ToList();
        }
        catch (Exception ex)
        {
            LangfuseTracing.MarkError(discoveryActivity, ex);
            throw;
        }
        finally
        {
            discoveryActivity?.Dispose();
        }
    }

    private static string BuildAgentInstructions(
        OrchestratorConfig config,
        IReadOnlyCollection<DiscoveredA2AAgent> agents,
        IReadOnlyCollection<DiscoveredMcpTool> mcpTools)
    {
        var builder = new StringBuilder();
        builder.AppendLine(config.Prompt.Trim());
        builder.AppendLine();
        builder.AppendLine("Runtime discovery snapshot:");

        if (agents.Count == 0)
        {
            builder.AppendLine("- No A2A agents were discovered.");
        }
        else
        {
            builder.AppendLine("- Discovered A2A agents:");
            foreach (var agent in agents)
            {
                builder.AppendLine(
                    $"  - {agent.Name}: {agent.DisplayName}. {agent.Description}");
                if (agent.Skills.Count > 0)
                {
                    builder.AppendLine(
                        $"    Skills: {string.Join(" | ", agent.Skills)}");
                }
            }
        }

        if (mcpTools.Count == 0)
        {
            builder.AppendLine("- No MCP tools were discovered.");
        }
        else
        {
            builder.AppendLine("- Discovered MCP tools:");
            foreach (var toolGroup in mcpTools.GroupBy(static tool => tool.ServerName))
            {
                builder.AppendLine(
                    $"  - {toolGroup.Key}: {string.Join(", ", toolGroup.Select(static tool => tool.ToolName))}");
            }
        }

        builder.AppendLine();
        builder.AppendLine("Operating rules:");
        builder.AppendLine("- Use discovered MCP tools directly when they can solve the request.");
        builder.AppendLine("- Use `delegate_to_agent` when a discovered A2A agent is a better specialist for a subtask.");
        builder.AppendLine("- When delegating, send a self-contained request and then synthesize the result for the user.");
        builder.AppendLine("- Never invent tools, agent names, skills, or capabilities that were not discovered at startup.");
        builder.AppendLine("- If discovery was partial, say that clearly instead of pretending a missing dependency is available.");
        return builder.ToString();
    }

    private static void EnsureResolvedEndpoint(string? endpoint, string subject)
    {
        if (!string.IsNullOrWhiteSpace(endpoint)
            && endpoint.Contains('$', StringComparison.Ordinal))
        {
            throw new InvalidOperationException(
                $"{subject} has an unresolved endpoint value: '{endpoint}'.");
        }
    }

    private static AgentInterface? ChooseA2aInterface(
        AgentCard card,
        string? preferredTransport)
    {
        var supportedInterfaces = card.SupportedInterfaces ?? [];
        if (supportedInterfaces.Count == 0)
        {
            return null;
        }

        var normalizedPreferredTransport = NormalizeIdentifier(preferredTransport ?? "jsonrpc");
        var preferred = supportedInterfaces.FirstOrDefault(candidate =>
            string.Equals(candidate.ProtocolVersion, "1.0", StringComparison.OrdinalIgnoreCase)
            && NormalizeIdentifier(candidate.ProtocolBinding) == normalizedPreferredTransport);
        if (preferred is not null)
        {
            return preferred;
        }

        preferred = supportedInterfaces.FirstOrDefault(candidate =>
            string.Equals(candidate.ProtocolVersion, "1.0", StringComparison.OrdinalIgnoreCase)
            && NormalizeIdentifier(candidate.ProtocolBinding) is "jsonrpc" or "http_json" or "http_jsonrpc" or "httpjson");
        if (preferred is not null)
        {
            return preferred;
        }

        return supportedInterfaces.FirstOrDefault(candidate =>
            string.Equals(candidate.ProtocolVersion, "1.0", StringComparison.OrdinalIgnoreCase));
    }

    private static bool MatchesToolFilters(string toolName, McpServerConfig serverConfig)
    {
        var normalizedToolName = NormalizeIdentifier(toolName);
        var allowedTools = serverConfig.AllowedTools
            .Select(NormalizeIdentifier)
            .ToHashSet(StringComparer.OrdinalIgnoreCase);
        var blockedTools = serverConfig.BlockedTools
            .Select(NormalizeIdentifier)
            .ToHashSet(StringComparer.OrdinalIgnoreCase);

        if (allowedTools.Count > 0 && !allowedTools.Contains(normalizedToolName))
        {
            return false;
        }

        if (blockedTools.Contains(normalizedToolName))
        {
            return false;
        }

        return true;
    }

    public static string ExtractMessageText(Message? message) =>
        message is null
            ? string.Empty
            : FormatMessageParts("message", message.Parts);

    private static string ExtractArtifactsText(IEnumerable<Artifact>? artifacts)
    {
        if (artifacts is null)
        {
            return string.Empty;
        }

        var builder = new StringBuilder();
        foreach (var artifact in artifacts)
        {
            var text = ExtractPartsText(artifact.Parts);
            if (string.IsNullOrWhiteSpace(text))
            {
                continue;
            }

            if (builder.Length > 0)
            {
                builder.AppendLine();
                builder.AppendLine();
            }

            builder.Append(text.Trim());
        }

        return builder.ToString().Trim();
    }

    public static string FormatMessageParts(string label, IEnumerable<Part> parts)
    {
        var text = ExtractPartsText(parts);
        return string.IsNullOrWhiteSpace(text)
            ? $"{label} returned no text content."
            : text;
    }

    public static string ExtractPartsText(IEnumerable<Part> parts)
    {
        var builder = new StringBuilder();
        foreach (var part in parts)
        {
            if (!string.IsNullOrWhiteSpace(part.Text))
            {
                if (builder.Length > 0)
                {
                    builder.AppendLine();
                }

                builder.Append(part.Text.Trim());
            }
        }

        return builder.ToString().Trim();
    }

    public static string NormalizeIdentifier(string? value) =>
        string.IsNullOrWhiteSpace(value)
            ? string.Empty
            : value.Trim().ToLowerInvariant().Replace('-', '_').Replace(' ', '_').Replace('+', '_');

    public static string NormalizeTaskState(TaskState state) =>
        state switch
        {
            TaskState.InputRequired => "input-required",
            TaskState.AuthRequired => "auth-required",
            TaskState.Canceled => "canceled",
            _ => NormalizeIdentifier(state.ToString()).Replace('_', '-'),
        };
}
