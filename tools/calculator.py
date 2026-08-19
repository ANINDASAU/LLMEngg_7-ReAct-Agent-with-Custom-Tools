import ast
import operator
from langchain_core.tools import tool


# Allowed mathematical operations
ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _safe_eval(node):
    """
    Recursively evaluate a mathematical AST safely.
    """

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numbers are allowed.")

    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)

        operation = ALLOWED_OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operator not allowed.")

        # Prevent extremely large exponent calculations
        if isinstance(node.op, ast.Pow) and abs(right) > 10:
            raise ValueError("Exponent too large.")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)

        operation = ALLOWED_OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operator not allowed.")

        return operation(operand)

    raise ValueError("Invalid mathematical expression.")


@tool
def calculate(expression: str) -> str:
    """
    Safely calculate a mathematical expression.

    Use this tool when the user asks for arithmetic or mathematical
    calculations.
    """

    try:
        tree = ast.parse(expression, mode="eval")

        result = _safe_eval(tree.body)

        return str(result)

    except Exception as e:
        return f"Calculation error: {str(e)}"