import pytest


# Add your test cases below
@pytest.mark.asyncio
async def test_greet_tool():
    from template_mcp_server.server import greet

    assert await greet("World") == "Hello, World!"
