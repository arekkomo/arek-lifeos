# Obsidian MCP Server Evaluation — 2026-06-04

## Evaluation Criteria
- Support for bidirectional sync (read + write)
- Graph traversal / traversal between linked notes
- Works filesystem-direct (no Obsidian app required)
- Active maintenance, community adoption
- Tool breadth for Arek&Co vault (~720 files)

## Candidates Evaluated

### graphthulhu (skridlevsky/graphthulhu)
- **Stars:** 162
- **Language:** Go (single binary, no Node.js dependency)
- **Backend:** Obsidian or Logseq — reads vault .md files directly via fs
- **Key tools:** `traverse`, `find_connections`, `get_links`, `link_pages`, `knowledge_gaps`, `topic_clusters`, `graph_overview`
- **Pros:** Explicit graph analytics, bidirectional linking, knowledge-gap detection, topic clustering, atomic writes
- **Cons:** Less popular, no built-in vector search (relies on wikilink graph only)
- **Verdict:** **Selected.** Best fit for Arek&Co — the graph tools (traverse, connections, clusters) match the stated need

### obsidian-mcp-seekstone (shaqmughal/seekstone)
- **Stars:** High downloads on npm (fast search benchmarked at 3.9ms)
- **Lang:** Node.js ≥22
- **Tools:** search (ranked excerpts read, list_notes, create_note, delete_note, move_note, append_note, patch_frontmatter
- **Pros:** 575× smaller payloads vs REST proxy, search is faster than most
- **Cons:** No graph traversal or bidirectional link tools — flat file search only
- **Verdict:** Excellent for read-heavy search, but no graph capability

### swarmvault (swarmclawai/swarmvault)
- **Stars:** 518
- **Lang:** Node.js ≥24
- **Tools:** graph, wiki, RAG, compile, query, context packs
- **Pros:** Full knowledge graph builder, Karpathy-inspired, hybrid search + embeddings
- **Cons:** Larger dependency chain (requires full compile pipeline, Ollama optional)
- **Verdict:** Powerful but heavyweight — better for building from scratch than for enhancing an existing vault

### contextplus (forloopcodes/contextplus)
- **Stars:** 1,915 (highest)
- **Lang:** TypeScript
- **Tools:** RAG, Tree-sitter AST, spectral clustering, Obsidian linking
- **Pros:** Most stars, strong AI agent support, community backing
- **Cons:** Primarily codebase-focused (Tree-sitter AST), not vault-specific
- **Verdict:** Overkill for markdown-only vault use

### obsidian-mcp-server (cyanheads/connorbritain)
- **Stars:** 2 (low)
- **Lang:** TypeScript
- **Tools:** "vault operations, graph analytics, advanced search, semantic tools"
- **Pros:** Has graph analytics and semantic search built-in
- **Cons:** Very low adoption, likely abandoned (only 2 stars as of 2026-06)
- **Verdict:** Skip

## Final Selection: graphthulhu

**Setup command:**
```bash
# Install binary
curl -sL https://github.com/skridlevsky/graphthulhu/releases/latest/download/graphthulhu-linux-amd64 -o /usr/local/bin/graphthulhu
chmod +x /usr/local/bin/graphthulhu

# Or via go install
go install github.com/skridlevsky/graphthulhu@latest
```

**For Hermes config.yaml:**
```yaml
mcp_servers:
  graphthulhu:
    command: "graphthulhu"
    args: ["serve"]
    env:
      GRAPHTHULHU_BACKEND: "obsidian"
      OBSIDIAN_VAULT_PATH: "/home/realityrove/Obsidian/Arek&Co"
```

**After install, restart Hermes — tools appear as `mcp_graphthulhu_*`:**
- `mcp_graphthulhu_get_page`, `mcp_graphthulhu_get_links`, `mcp_graphthulhu_get_references`
- `mcp_graphthulhu_traverse`, `mcp_graphthulhu_find_connections`
- `mcp_graphthulhu_list_pages`, `mcp_graphthulhu_search`, `mcp_graphthulhu_query_properties`
- `mcp_graphthulhu_link_pages`, `mcp_graphthulhu_update_block`
- `mcp_graphthulhu_knowledge_gaps`, `mcp_graphthulhu_topic_clusters`, `mcp_graphthulhu_graph_overview`

## Key Pitfalls
- graphthulhu requires Go binary or `go install`. NOT an npm package, NOT a Node.js server.
- For Logseq backend, requires the Logseq HTTP API server running. Obsidian backend is filesystem-direct — no Obsidian app needed.
- In-memory index rebuilds on every mutation. Large vaults (>10k notes) will be slow on startup.
- File watching uses fsnotify — not reliable on network drives or WSL
- All writes go through atomic temp-file renames

## Comparison Summary Table

| Server | Graph Traversal | Backlink Index | Semantic Search | Vault-Focused | Install |
|---|---|---|---|---|---|
| graphthulhu | ✅ traverse, connections | ✅ wikilink resolution | ❌ (wikilinks only) | ✅ | Go binary |
| seekstone | ❌ | partial (search only) | ✅ excerpt-based | ✅ | npx Node |
| swarmvault | ✅ custom graph | ✅ | ✅ hybrid FTS+embed | ⚠️ general wiki | npm Node |
| contextplus | ⚠️ spectral clustering | ⚠️ code focus | ✅ RAG | ❌ code repo | npm Node |
| obsidian-mcp | ✅ | ✅ | ⚠️ limited | ✅ | npm Node (abandoned) |
