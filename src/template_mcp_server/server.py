from mcp.server.fastmcp import FastMCP

server = FastMCP("template_mcp_server")


# Add your mcp tools and resources here
@server.tool()
async def greet(name: str) -> str:
    return f"Hello, {name}!"


def main():
    server.run("stdio")
