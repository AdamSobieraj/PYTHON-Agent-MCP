using System.ComponentModel;
using System.Diagnostics;
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

        Activity? delegationActivity = null;
        Activity? remoteAgentActivity = null;
        logger.LogInformation(
            "Delegating request to A2A agent {AgentName} at {EndpointUrl}",
            agent.Name,
            agent.EndpointUrl);

        try
        {
            delegationActivity = LangfuseTracing.StartToolActivity(
                "orchestrator.delegate_to_agent",
                input: requestText,
                observationMetadata: new Dictionary<string, object?>
                {
                    ["agent_name"] = agent.Name,
                    ["display_name"] = agent.DisplayName,
                    ["endpoint_url"] = agent.EndpointUrl,
                });

            var client = new A2AClient(new Uri(agent.EndpointUrl));
            remoteAgentActivity = LangfuseTracing.StartAgentActivity(
                "orchestrator.remote_a2a_agent",
                input: requestText,
                observationMetadata: new Dictionary<string, object?>
                {
                    ["agent_name"] = agent.Name,
                    ["display_name"] = agent.DisplayName,
                    ["endpoint_url"] = agent.EndpointUrl,
                    ["protocol_binding"] = agent.ProtocolBinding,
                });
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

            var formattedResponse = runtime.FormatDelegatedResponse(agent, response);
            LangfuseTracing.SetOutput(remoteAgentActivity, formattedResponse);
            LangfuseTracing.SetOutput(delegationActivity, formattedResponse);
            return formattedResponse;
        }
        catch (Exception ex)
        {
            LangfuseTracing.MarkError(remoteAgentActivity, ex);
            LangfuseTracing.MarkError(delegationActivity, ex);
            throw;
        }
        finally
        {
            remoteAgentActivity?.Dispose();
            delegationActivity?.Dispose();
        }
    }
}
