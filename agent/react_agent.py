from langgraph.prebuilt import create_react_agent
from langchain_ollama import ChatOllama

from memory import create_memory
from tools import (
    calculate,
    define_word,
    get_current_datetime,
)


def create_agent():
    """
    Create and return the LangGraph ReAct agent.
    """

    # --------------------------------------------------
    # 1. Load Ollama model
    # --------------------------------------------------

    model = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    # --------------------------------------------------
    # 2. Register custom tools
    # --------------------------------------------------

    tools = [
        calculate,
        define_word,
        get_current_datetime,
    ]

    # --------------------------------------------------
    # 3. Create memory/checkpointer
    # --------------------------------------------------

    memory = create_memory()

    # --------------------------------------------------
    # 4. Create ReAct agent
    # --------------------------------------------------

    agent = create_react_agent(
        model=model,
        tools=tools,
        checkpointer=memory,
        prompt=(
            "You are a helpful assistant using the ReAct pattern. "
            "Answer general knowledge questions directly. Use calculate "
            "only for arithmetic, define_word only when the user explicitly "
            "asks for a word or concept definition, and "
            "get_current_datetime only for the current date or time."
        ),
    )

    return agent