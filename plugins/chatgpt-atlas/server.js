const http = require("node:http");
const { URL } = require("node:url");

const OWNER = "cellrishi-code";
const REPO = "claude-skills-atlas";
const PORT = Number(process.env.PORT || 8787);
const ALLOWED_TYPES = new Set(["skill", "prompt", "workflow", "agent", "template"]);

function send(res, status, data) {
  const body = JSON.stringify(data);
  res.writeHead(status, {
    "content-type": "application/json; charset=utf-8",
    "access-control-allow-origin": "*",
    "cache-control": "no-store"
  });
  res.end(body);
}

async function github(path) {
  const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${path}`;
  const response = await fetch(url, {
    headers: {
      "accept": "application/vnd.github+json",
      "user-agent": "claude-skills-atlas-chatgpt-plugin"
    }
  });

  if (!response.ok) {
    throw new Error(`GitHub returned ${response.status}`);
  }

  return response.json();
}

function inferType(path) {
  const first = path.split("/")[0];
  return ALLOWED_TYPES.has(first.replace(/s$/, "")) ? first.replace(/s$/, "") : null;
}

async function collectFiles(path, results, maxFiles = 200) {
  if (results.length >= maxFiles) return;
  const entries = await github(path);

  if (!Array.isArray(entries)) {
    if (path.endsWith(".md")) {
      results.push({ path, type: inferType(path), name: path.split("/").pop() });
    }
    return;
  }

  for (const entry of entries) {
    if (results.length >= maxFiles) break;
    if (entry.type === "dir") {
      await collectFiles(entry.path, results, maxFiles);
    } else if (entry.type === "file" && entry.path.endsWith(".md")) {
      const type = inferType(entry.path);
      if (type) {
        results.push({
          path: entry.path,
          type,
          name: entry.name.replace(/\.md$/, ""),
          url: entry.html_url
        });
      }
    }
  }
}

async function main(req, res) {
  const url = new URL(req.url, `http://localhost:${PORT}`);

  if (req.method !== "GET") {
    return send(res, 405, { error: "Only GET is supported." });
  }

  if (url.pathname === "/health") {
    return send(res, 200, { status: "ok", repository: `${OWNER}/${REPO}` });
  }

  try {
    if (url.pathname === "/resources") {
      const q = (url.searchParams.get("q") || "").toLowerCase().trim();
      const requestedType = url.searchParams.get("type");
      const limit = Math.min(Math.max(Number(url.searchParams.get("limit") || 10), 1), 50);

      if (requestedType && !ALLOWED_TYPES.has(requestedType)) {
        return send(res, 400, { error: "Invalid resource type." });
      }

      const resources = [];
      for (const root of ["skills", "prompts", "workflows", "agents", "templates"]) {
        if (requestedType && root.replace(/s$/, "") !== requestedType) continue;
        await collectFiles(root, resources);
      }

      const filtered = resources
        .filter(item => !q || `${item.name} ${item.path}`.toLowerCase().includes(q))
        .slice(0, limit);

      return send(res, 200, { results: filtered, count: filtered.length });
    }

    if (url.pathname === "/resource") {
      const path = url.searchParams.get("path");
      if (!path || path.includes("..") || !ALLOWED_TYPES.has(path.split("/")[0].replace(/s$/, ""))) {
        return send(res, 400, { error: "A valid public Atlas resource path is required." });
      }

      const data = await github(path);
      if (data.type !== "file" || typeof data.content !== "string") {
        return send(res, 404, { error: "Resource not found." });
      }

      const content = Buffer.from(data.content, "base64").toString("utf8");
      return send(res, 200, { path, content, url: data.html_url });
    }

    return send(res, 404, { error: "Not found." });
  } catch (error) {
    return send(res, 502, { error: "Unable to read the public Atlas repository." });
  }
}

http.createServer(main).listen(PORT, () => {
  console.log(`Claude Skills Atlas plugin listening on port ${PORT}`);
});
