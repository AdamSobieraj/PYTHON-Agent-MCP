using A2A;
using A2A.AspNetCore;

using BusinessAgent.Orchestrator.Agents;
using BusinessAgent.Orchestrator.Configuration;
using BusinessAgent.Orchestrator.Models;
using BusinessAgent.Orchestrator.Services;

var bindUrl = Environment.GetEnvironmentVariable("ORCHESTRATOR_BIND_URL")
    ?? "http://0.0.0.0:10110";
var publicBaseUrl = ResolvePublicBaseUrl(
    bindUrl,
    Environment.GetEnvironmentVariable("ORCHESTRATOR_PUBLIC_BASE_URL"));

var builder = WebApplication.CreateBuilder(args);
builder.WebHost.UseUrls(bindUrl);
builder.Logging.ClearProviders();
builder.Logging.AddSimpleConsole(options =>
{
    options.SingleLine = true;
    options.TimestampFormat = "HH:mm:ss ";
});
builder.Services.AddLangfuseOpenTelemetry();

builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.AllowAnyOrigin()
            .AllowAnyMethod()
            .AllowAnyHeader();
    });
});

builder.Services.AddHttpClient(nameof(LangfuseOrchestratorConfigProvider));
builder.Services.AddSingleton<JsonOrchestratorConfigProvider>();
builder.Services.AddSingleton<IOrchestratorConfigProvider, LangfuseOrchestratorConfigProvider>();
builder.Services.AddSingleton<OrchestratorRuntime>();
builder.Services.AddSingleton<AgUiThreadSessionStore>();
builder.Services.AddSingleton(sp =>
    new AgUiBridgeService(
        publicBaseUrl,
        sp.GetRequiredService<AgUiThreadSessionStore>(),
        sp.GetRequiredService<ILogger<AgUiBridgeService>>()));

var agentCard = AgentCardFactory.Build(publicBaseUrl);
builder.Services.AddA2AAgent<OrchestratorA2AAgent>(agentCard);

var app = builder.Build();

app.UseCors();

app.MapGet("/", () => Results.Ok(new
{
    name = agentCard.Name,
    postPath = "/",
    healthz = "/healthz",
    catalog = "/catalog",
    a2a = new
    {
        jsonrpc = "/a2a/jsonrpc",
        rest = "/a2a/rest",
        agentCard = "/.well-known/agent-card.json",
    },
    forwardedProps = new
    {
        a2a = new
        {
            url = $"{publicBaseUrl}/a2a/jsonrpc",
            transport = "JSONRPC",
        },
    },
}));

app.MapGet("/healthz", () => Results.Ok(new
{
    ok = true,
    service = "business-agent-orchestrator",
}));

app.MapGet("/catalog", async (
    OrchestratorRuntime runtime,
    CancellationToken cancellationToken) =>
{
    await runtime.InitializeAsync(cancellationToken);
    return Results.Ok(runtime.Snapshot);
});

app.MapPost("/", (
    RunAgentInput input,
    HttpRequest request,
    AgUiBridgeService bridge,
    CancellationToken cancellationToken) =>
{
    var encoder = new AgUiEventEncoder(request.Headers.Accept.ToString());

    return Results.Stream(
        async responseStream =>
        {
            await foreach (var payload in bridge.StreamEventsAsync(input, cancellationToken))
            {
                var chunk = encoder.Encode(payload);
                await responseStream.WriteAsync(chunk.AsMemory(0, chunk.Length), cancellationToken);
                await responseStream.FlushAsync(cancellationToken);
            }
        },
        encoder.ContentType);
});

app.MapA2A("/a2a/jsonrpc");
app.MapHttpA2A(
    app.Services.GetRequiredService<IA2ARequestHandler>(),
    agentCard,
    "/a2a/rest");
app.MapWellKnownAgentCard(agentCard);

var runtime = app.Services.GetRequiredService<OrchestratorRuntime>();
await runtime.InitializeAsync();
AgentCardFactory.ApplyTo(agentCard, publicBaseUrl, runtime.RuntimeConfig);

app.Run();

static string ResolvePublicBaseUrl(string bindUrl, string? configuredPublicBaseUrl)
{
    if (!string.IsNullOrWhiteSpace(configuredPublicBaseUrl))
    {
        return configuredPublicBaseUrl.TrimEnd('/');
    }

    if (!Uri.TryCreate(bindUrl, UriKind.Absolute, out var bindUri))
    {
        return "http://localhost:10110";
    }

    var host = bindUri.Host is "0.0.0.0" or "::"
        ? "localhost"
        : bindUri.Host;
    var builder = new UriBuilder(bindUri)
    {
        Host = host,
    };
    return builder.Uri.ToString().TrimEnd('/');
}
