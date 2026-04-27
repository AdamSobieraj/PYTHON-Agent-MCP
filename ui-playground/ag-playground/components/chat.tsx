"use client";

import { useMemo } from "react";
import { CopilotKit } from "@copilotkit/react-core";
import { CopilotChat } from "@copilotkit/react-ui";

export default function Chat() {
  const threadId = useMemo(() => {
    return `business-agent-${crypto.randomUUID()}`;
  }, []);

  return (
    <div className="h-full min-h-0">
      <CopilotKit
        runtimeUrl="/api/copilotkit"
        agent="orchestrator"
        threadId={threadId}
      >
        <div className="h-full min-h-0">
          <CopilotChat
            labels={{
              title: "Business Agent Orchestrator",
              initial:
                'Ask anything the orchestrator can solve through its loaded MCP tools and A2A agents.\n\nTry:\n- "What agents and tools do you have available?"\n- "Use the knowledge base to summarize our internal process"\n- "Delegate deeper research to the research agent if needed"',
            }}
            className="h-full"
          />
        </div>
      </CopilotKit>
    </div>
  );
}
