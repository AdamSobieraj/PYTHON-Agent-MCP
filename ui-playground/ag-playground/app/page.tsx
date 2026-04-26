"use client";

import { useEffect, useState } from "react";
import dynamic from "next/dynamic";

const Chat = dynamic(() => import("@/components/chat"), {
  ssr: false,
  loading: () => (
    <div className="flex h-full items-center justify-center px-6 text-sm text-[#57575B]">
      Loading chat...
    </div>
  ),
});

type CatalogAgent = {
  name: string;
  displayName: string;
  description: string;
  endpointUrl: string;
  protocolBinding: string;
  skills: string[];
};

type CatalogTool = {
  serverName: string;
  toolName: string;
  description: string;
};

type CatalogSnapshot = {
  loadedAt: string;
  configPath: string;
  a2aAgents: CatalogAgent[];
  mcpTools: CatalogTool[];
  warnings: string[];
};

const orchestratorBaseUrl =
  (
    process.env.NEXT_PUBLIC_ORCHESTRATOR_URL || "http://localhost:10111"
  ).replace(/\/$/, "");

export default function Home() {
  const [catalog, setCatalog] = useState<CatalogSnapshot | null>(null);
  const [catalogError, setCatalogError] = useState<string | null>(null);
  const [isCatalogLoading, setIsCatalogLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;

    async function loadCatalog() {
      setIsCatalogLoading(true);
      setCatalogError(null);

      try {
        const response = await fetch(`${orchestratorBaseUrl}/catalog`);
        if (!response.ok) {
          throw new Error(`Catalog request failed with ${response.status}`);
        }

        const payload = (await response.json()) as CatalogSnapshot;
        if (!cancelled) {
          setCatalog(payload);
        }
      } catch (error) {
        if (!cancelled) {
          setCatalog(null);
          setCatalogError(
            error instanceof Error ? error.message : "Unknown catalog error",
          );
        }
      } finally {
        if (!cancelled) {
          setIsCatalogLoading(false);
        }
      }
    }

    loadCatalog();

    return () => {
      cancelled = true;
    };
  }, []);

  const toolsByServer = (catalog?.mcpTools || []).reduce<
    Record<string, CatalogTool[]>
  >((accumulator, tool) => {
    if (!accumulator[tool.serverName]) {
      accumulator[tool.serverName] = [];
    }

    accumulator[tool.serverName].push(tool);
    return accumulator;
  }, {});

  return (
    <div className="relative flex min-h-screen overflow-hidden bg-[#DEDEE9] p-2">
      <div
        className="absolute left-[1040px] top-[11px] z-0 h-[445px] w-[445px] rounded-full"
        style={{ background: "rgba(255, 172, 77, 0.2)", filter: "blur(103px)" }}
      />
      <div
        className="absolute left-[1339px] top-[625px] z-0 h-[609px] w-[609px] rounded-full"
        style={{ background: "#C9C9DA", filter: "blur(103px)" }}
      />
      <div
        className="absolute left-[670px] top-[-365px] z-0 h-[609px] w-[609px] rounded-full"
        style={{ background: "#C9C9DA", filter: "blur(103px)" }}
      />
      <div
        className="absolute left-[128px] top-[331px] z-0 h-[445px] w-[445px] rounded-full"
        style={{
          background: "rgba(255, 243, 136, 0.3)",
          filter: "blur(103px)",
        }}
      />

      <div className="z-10 flex flex-1 gap-2 overflow-hidden">
        <div className="flex w-[450px] flex-shrink-0 flex-col overflow-hidden rounded-lg border-2 border-white bg-white/50 shadow-elevation-lg backdrop-blur-md">
          <div className="border-b border-[#DBDBE5] p-6">
            <h1 className="mb-1 text-2xl font-semibold text-[#010507]">
              Business Agent UI
            </h1>
            <p className="text-sm leading-relaxed text-[#57575B]">
              AG-UI playground connected to the .NET orchestrator.
            </p>
            <p className="mt-1 text-xs text-[#838389]">
              Endpoint: <span className="font-medium">{orchestratorBaseUrl}</span>
            </p>
          </div>

          <div className="flex-1 overflow-hidden">
            <Chat />
          </div>
        </div>

        <div className="flex-1 overflow-y-auto rounded-lg bg-white/30 backdrop-blur-sm">
          <div className="mx-auto p-8">
            <div className="mb-8">
              <h2 className="mb-2 text-3xl font-semibold text-[#010507]">
                Runtime Catalog
              </h2>
              <p className="text-[#57575B]">
                The orchestrator loads its A2A agents and MCP tools at startup.
                This panel reads the live catalog from <code>/catalog</code>.
              </p>
            </div>

            <div className="mb-6 rounded-xl border-2 border-[#DBDBE5] bg-white/60 p-6 shadow-elevation-md backdrop-blur-md">
              <div className="flex flex-wrap items-center gap-3">
                <span className="rounded-full border border-emerald-300 bg-emerald-50 px-3 py-1 text-xs font-semibold text-emerald-700">
                  AG-UI: POST /
                </span>
                <span className="rounded-full border border-sky-300 bg-sky-50 px-3 py-1 text-xs font-semibold text-sky-700">
                  A2A: /a2a/jsonrpc
                </span>
                <span className="rounded-full border border-violet-300 bg-violet-50 px-3 py-1 text-xs font-semibold text-violet-700">
                  Agent Card: /.well-known/agent-card.json
                </span>
              </div>
              <p className="mt-4 text-sm text-[#57575B]">
                Start the .NET orchestrator first, then refresh this page if the
                catalog is unavailable.
              </p>
            </div>

            {isCatalogLoading && (
              <div className="rounded-xl border-2 border-dashed border-[#DBDBE5] bg-white/60 p-8 text-[#57575B] shadow-elevation-sm backdrop-blur-md">
                Loading orchestrator catalog...
              </div>
            )}

            {!isCatalogLoading && catalogError && (
              <div className="rounded-xl border border-rose-300 bg-rose-50 p-6 text-rose-800 shadow-elevation-sm">
                <h3 className="mb-2 text-lg font-semibold">Catalog unavailable</h3>
                <p className="text-sm">{catalogError}</p>
              </div>
            )}

            {!isCatalogLoading && catalog && (
              <div className="space-y-6">
                <div className="rounded-xl border-2 border-[#DBDBE5] bg-white/60 p-6 shadow-elevation-md backdrop-blur-md">
                  <h3 className="mb-3 text-xl font-semibold text-[#010507]">
                    Startup Summary
                  </h3>
                  <div className="grid gap-3 md:grid-cols-3">
                    <div className="rounded-lg bg-white/80 p-4">
                      <p className="text-xs font-semibold uppercase tracking-wide text-[#838389]">
                        Loaded At
                      </p>
                      <p className="mt-1 text-sm text-[#010507]">
                        {new Date(catalog.loadedAt).toLocaleString()}
                      </p>
                    </div>
                    <div className="rounded-lg bg-white/80 p-4">
                      <p className="text-xs font-semibold uppercase tracking-wide text-[#838389]">
                        A2A Agents
                      </p>
                      <p className="mt-1 text-sm text-[#010507]">
                        {catalog.a2aAgents.length}
                      </p>
                    </div>
                    <div className="rounded-lg bg-white/80 p-4">
                      <p className="text-xs font-semibold uppercase tracking-wide text-[#838389]">
                        MCP Tools
                      </p>
                      <p className="mt-1 text-sm text-[#010507]">
                        {catalog.mcpTools.length}
                      </p>
                    </div>
                  </div>
                  <p className="mt-4 text-xs text-[#838389]">
                    Config file: {catalog.configPath}
                  </p>
                </div>

                <div className="rounded-xl border-2 border-[#DBDBE5] bg-white/60 p-6 shadow-elevation-md backdrop-blur-md">
                  <h3 className="mb-4 text-xl font-semibold text-[#010507]">
                    Discovered A2A Agents
                  </h3>

                  {catalog.a2aAgents.length === 0 && (
                    <p className="text-sm text-[#57575B]">
                      No A2A agents were discovered at startup.
                    </p>
                  )}

                  <div className="space-y-4">
                    {catalog.a2aAgents.map((agent) => (
                      <div key={agent.name} className="rounded-lg bg-white/80 p-4">
                        <div className="flex flex-wrap items-center gap-2">
                          <h4 className="text-lg font-semibold text-[#010507]">
                            {agent.displayName || agent.name}
                          </h4>
                          <span className="rounded-full border border-sky-300 bg-sky-50 px-2 py-1 text-xs font-semibold text-sky-700">
                            {agent.protocolBinding}
                          </span>
                        </div>
                        <p className="mt-2 text-sm text-[#57575B]">
                          {agent.description || "No description provided."}
                        </p>
                        <p className="mt-2 text-xs text-[#838389]">
                          {agent.endpointUrl}
                        </p>
                        {agent.skills.length > 0 && (
                          <div className="mt-3 flex flex-wrap gap-2">
                            {agent.skills.map((skill) => (
                              <span
                                key={`${agent.name}-${skill}`}
                                className="rounded-full border border-emerald-300 bg-emerald-50 px-2 py-1 text-xs font-medium text-emerald-700"
                              >
                                {skill}
                              </span>
                            ))}
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>

                <div className="rounded-xl border-2 border-[#DBDBE5] bg-white/60 p-6 shadow-elevation-md backdrop-blur-md">
                  <h3 className="mb-4 text-xl font-semibold text-[#010507]">
                    Discovered MCP Tools
                  </h3>

                  {Object.keys(toolsByServer).length === 0 && (
                    <p className="text-sm text-[#57575B]">
                      No MCP tools were discovered at startup.
                    </p>
                  )}

                  <div className="space-y-4">
                    {Object.entries(toolsByServer).map(([serverName, tools]) => (
                      <div key={serverName} className="rounded-lg bg-white/80 p-4">
                        <div className="mb-3 flex items-center gap-2">
                          <h4 className="text-lg font-semibold text-[#010507]">
                            {serverName}
                          </h4>
                          <span className="rounded-full border border-amber-300 bg-amber-50 px-2 py-1 text-xs font-semibold text-amber-700">
                            {tools.length} tools
                          </span>
                        </div>
                        <div className="grid gap-3 md:grid-cols-2">
                          {tools.map((tool) => (
                            <div
                              key={`${tool.serverName}-${tool.toolName}`}
                              className="rounded-lg border border-[#DBDBE5] bg-white p-3"
                            >
                              <p className="text-sm font-semibold text-[#010507]">
                                {tool.toolName}
                              </p>
                              <p className="mt-1 text-xs text-[#57575B]">
                                {tool.description || "No description provided."}
                              </p>
                            </div>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                {catalog.warnings.length > 0 && (
                  <div className="rounded-xl border border-amber-300 bg-amber-50 p-6 shadow-elevation-sm">
                    <h3 className="mb-3 text-lg font-semibold text-amber-900">
                      Startup Warnings
                    </h3>
                    <div className="space-y-2">
                      {catalog.warnings.map((warning, index) => (
                        <p key={`${warning}-${index}`} className="text-sm text-amber-800">
                          {warning}
                        </p>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
