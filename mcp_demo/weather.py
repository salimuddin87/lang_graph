from mcp.server.fastmcp import FastMCP


mcp = FastMCP("weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get the weather of my location
    :param location:
    :return:
    """
    return "It's raining in Hyderabad"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
