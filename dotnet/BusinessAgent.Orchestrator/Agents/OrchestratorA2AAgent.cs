using System.Text;

using A2A;

using BusinessAgent.Orchestrator.Services;

namespace BusinessAgent.Orchestrator.Agents;

public sealed class OrchestratorA2AAgent(
    OrchestratorRuntime runtime,
    ILogger<OrchestratorA2AAgent> logger) : IAgentHandler
{
    public async Task ExecuteAsync(
        RequestContext context,
        AgentEventQueue eventQueue,
        CancellationToken cancellationToken)
    {
        var updater = new TaskUpdater(eventQueue, context.TaskId, context.ContextId);

        await updater.SubmitAsync(cancellationToken);
        await updater.StartWorkAsync(
            CreateAgentMessage(
                context,
                "The orchestrator is loading discovery metadata and preparing the request."),
            cancellationToken);

        try
        {
            await runtime.InitializeAsync(cancellationToken);

            var requestText = BuildOrchestratorRequest(context);
            if (string.IsNullOrWhiteSpace(requestText))
            {
                await updater.RequireInputAsync(
                    CreateAgentMessage(context, "Please send a text request for the orchestrator."),
                    cancellationToken);
                return;
            }

            var result = await runtime.GenerateResponseAsync(
                requestText,
                cancellationToken);

            if (string.IsNullOrWhiteSpace(result))
            {
                result = "The orchestrator completed without returning text output.";
            }

            await updater.AddArtifactAsync(
                [Part.FromText(result)],
                name: "orchestrator-response",
                description: "Final response from the orchestrator.",
                cancellationToken: cancellationToken);
            await updater.CompleteAsync(cancellationToken: cancellationToken);
        }
        catch (Exception ex)
        {
            logger.LogError(ex, "The orchestrator failed while handling task {TaskId}", context.TaskId);
            await updater.FailAsync(
                CreateAgentMessage(context, $"The orchestrator failed: {ex.Message}"),
                cancellationToken);
        }
    }

    private static string BuildOrchestratorRequest(RequestContext context)
    {
        var currentRequest = context.UserText?.Trim();
        if (string.IsNullOrWhiteSpace(currentRequest))
        {
            return string.Empty;
        }

        var builder = new StringBuilder();
        if (context.Task?.History is { Count: > 0 } history)
        {
            builder.AppendLine("Conversation history:");
            foreach (var message in history)
            {
                var role = message.Role == Role.Agent ? "assistant" : "user";
                var text = OrchestratorRuntime.ExtractMessageText(message);
                if (string.IsNullOrWhiteSpace(text))
                {
                    continue;
                }

                builder.AppendLine($"- {role}: {text}");
            }

            builder.AppendLine();
        }

        builder.AppendLine("Latest user request:");
        builder.Append(currentRequest);
        return builder.ToString().Trim();
    }

    private static Message CreateAgentMessage(RequestContext context, string text) =>
        new()
        {
            Role = Role.Agent,
            MessageId = Guid.NewGuid().ToString("N"),
            ContextId = context.ContextId,
            TaskId = context.TaskId,
            Parts = [Part.FromText(text)],
        };
}
