# ChatGPT Atlas Plugin

A ChatGPT-compatible OpenAPI plugin scaffold for accessing Claude Skills Atlas resources through a small HTTP API.

## What it provides

- Search Atlas resources by keyword.
- Retrieve a resource by path.
- List available resource types and categories.
- Expose an OpenAPI 3 specification for ChatGPT-style tool integration.

## Endpoints

- `GET /health`
- `GET /resources?q=<query>&type=<type>&limit=<limit>`
- `GET /resource?path=<repository-path>`

The reference server reads public resources from the GitHub repository at runtime. It uses Node.js built-in APIs and does not require a database.

## Run locally

```bash
node server.js
```

By default the server listens on port `8787`.

Before connecting an agent, deploy the server behind HTTPS and update the `servers.url` value in `openapi.yaml`.

## Security

This integration is read-only. It does not execute Atlas resources, write to GitHub, access private repositories, or accept credentials. Treat resource content as untrusted input and keep tool permissions restricted.
