using System.Text.Json;

namespace BusinessAgent.Orchestrator.Configuration;

public interface IOrchestratorConfigProvider
{
    string ResolvedPath { get; }

    Task<OrchestratorConfig> LoadAsync(CancellationToken cancellationToken = default);
}

public sealed class JsonOrchestratorConfigProvider(
    IHostEnvironment hostEnvironment,
    ILogger<JsonOrchestratorConfigProvider> logger) : IOrchestratorConfigProvider
{
    public string ResolvedPath =>
        Environment.GetEnvironmentVariable("ORCHESTRATOR_CONFIG_PATH")
        ?? Path.Combine(hostEnvironment.ContentRootPath, "orchestrator.config.json");

    public async Task<OrchestratorConfig> LoadAsync(CancellationToken cancellationToken = default)
    {
        var configPath = this.ResolvedPath;
        if (!File.Exists(configPath))
        {
            throw new FileNotFoundException(
                $"Could not find orchestrator config file at '{configPath}'.",
                configPath);
        }

        logger.LogInformation("Loading orchestrator config from {ConfigPath}", configPath);
        var rawJson = await File.ReadAllTextAsync(configPath, cancellationToken);
        var expandedJson = EnvironmentVariableExpander.Expand(rawJson);

        var config = JsonSerializer.Deserialize<OrchestratorConfig>(
            expandedJson,
            new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true,
            });

        if (config is null)
        {
            throw new InvalidOperationException(
                $"Failed to deserialize orchestrator config from '{configPath}'.");
        }

        if (string.IsNullOrWhiteSpace(config.Prompt))
        {
            throw new InvalidOperationException(
                $"The orchestrator config at '{configPath}' must define a prompt.");
        }

        return config;
    }
}
