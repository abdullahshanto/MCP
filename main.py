
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract second number from first."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide first number by second."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Calculate power."""
    return base ** exponent

@mcp.tool()
def modulus(a: float, b: float) -> float:
    """Calculate remainder."""
    if b == 0:
        raise ValueError("Cannot perform modulus by zero")
    return a % b

