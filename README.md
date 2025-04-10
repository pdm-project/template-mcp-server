# template-mcp-server

_An example MCP server developed by Python and PDM._

## Usage with Claude Desktop

Add the following to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "template-mcp-server": {
      "command": "uvx",
      "args": [
        "template-mcp-server"
      ]
    }
  }
}
```

It requires `uv` to be installed on your machine. Check the [official documentation](https://docs.astral.sh/uv/getting-started/installation/) for installation guides.

## Available Tools

<!-- List all tools and descriptions here -->

## Development

```shell
pdm install
pdm dev
```
