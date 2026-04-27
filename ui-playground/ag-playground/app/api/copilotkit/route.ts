import {
  CopilotRuntime,
  ExperimentalEmptyAdapter,
  copilotRuntimeNextJSAppRouterEndpoint,
} from "@copilotkit/runtime";
import { HttpAgent } from "@ag-ui/client";
import { NextRequest } from "next/server";

/**
 * CopilotKit proxy for the .NET Business Agent Orchestrator.
 *
 * The orchestrator already exposes AG-UI at POST /, so the frontend only needs
 * a thin runtime that forwards AG-UI traffic to that endpoint.
 */
export async function POST(request: NextRequest) {
  const orchestratorUrl = (
    process.env.ORCHESTRATOR_URL ||
    process.env.NEXT_PUBLIC_ORCHESTRATOR_URL ||
    "http://localhost:10111"
  ).replace(/\/$/, "");

  const orchestrationAgent = new HttpAgent({
    url: orchestratorUrl,
  });

  const runtime = new CopilotRuntime({
    agents: {
      orchestrator: orchestrationAgent,
    },
  });

  const { handleRequest } = copilotRuntimeNextJSAppRouterEndpoint({
    runtime,
    serviceAdapter: new ExperimentalEmptyAdapter(),
    endpoint: "/api/copilotkit",
  });

  return handleRequest(request);
}
