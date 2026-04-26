using System.ComponentModel;
using System.Text;

using A2A;

using Microsoft.SemanticKernel;

namespace BusinessAgent.Orchestrator.Services;

public sealed class A2ADelegationPlugin(
    OrchestratorRuntime runtime,
    ILogger<A2ADelegationPlugin> logger)
{
    [KernelFunction("delegate_to_agent")]
    [Description("Delegate a self-contained subtask to one of the discovered A2A agents.")]
    public async Task<string> DelegateToAgentAsync(
        [Description("Exact discovered A2A agent name from the runtime catalog.")]
        string agentName,
        [Description("The self-contained task, question, or sub-problem to send to that agent.")]
        string task,
        [Description("Optional extra context or constraints for the delegated task.")]
        string? context = null)
    {
        var agent = runtime.TryGetA2aAgent(agentName);
        if (agent is null)
        {
            var availableAgents = string.Join(", ", runtime.GetKnownA2aAgentNames());
            throw new InvalidOperationException(
                $"A2A agent '{agentName}' was not discovered. Available agents: {availableAgents}.");
        }

        var requestText = string.IsNullOrWhiteSpace(context)
            ? task.Trim()
            : $"{task.Trim()}\n\nAdditional context:\n{context.Trim()}";

        logger.LogInformation(
            "Delegating request to A2A agent {AgentName} at {EndpointUrl}",
            agent.Name,
            agent.EndpointUrl);

        var client = new A2AClient(new Uri(agent.EndpointUrl));
        var response = await client.SendMessageAsync(
            new SendMessageRequest
            {
                Message = new Message
                {
                    Role = Role.User,
                    MessageId = Guid.NewGuid().ToString("N"),
                    ContextId = Guid.NewGuid().ToString("N"),
                    Parts = [Part.FromText(requestText)],
                },
            });

        return runtime.FormatDelegatedResponse(agent, response);
    }
}
