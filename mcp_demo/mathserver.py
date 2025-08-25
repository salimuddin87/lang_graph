from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two number
    :param a:
    :param b:
    :return:
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two number
    :param a:
    :param b:
    :return:
    """
    return a * b


if __name__ == "__main__":
    # Use Standard input/output (stdin and stdout) to receive and respond to tool function calls
    mcp.run(transport="stdio")
