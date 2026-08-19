from datetime import datetime
from langchain_core.tools import tool


@tool
def get_current_datetime() -> str:
    """
    Return the current local date and time.

    Use this tool when the user asks about the current date,
    current time, today, or the current datetime.
    """

    current_time = datetime.now()

    return current_time.strftime(
        "%Y-%m-%d %H:%M:%S"
    )