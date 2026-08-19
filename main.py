from agent import create_agent


def print_separator(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def display_agent_response(response):

    print("\n" + "-" * 70)
    print("REACT TRACE")
    print("-" * 70)

    messages = response["messages"]

    for message in messages:

        message_type = type(message).__name__

        # --------------------------------------------------
        # User message
        # --------------------------------------------------

        if message_type == "HumanMessage":

            print("\n[USER]")
            print(message.content)

        # --------------------------------------------------
        # AI message
        # --------------------------------------------------

        elif message_type == "AIMessage":

            # Tool calls made by the model
            if getattr(message, "tool_calls", None):

                print("\n[AGENT DECISION]")

                for tool_call in message.tool_calls:

                    tool_name = tool_call["name"]
                    tool_args = tool_call["args"]

                    print(
                        f"Tool required: {tool_name}"
                    )

                    print(
                        f"Action: {tool_name}({tool_args})"
                    )

            # Final answer
            elif message.content:

                print("\n[FINAL ANSWER]")
                print(message.content)

        # --------------------------------------------------
        # Tool result
        # --------------------------------------------------

        elif message_type == "ToolMessage":

            print("\n[OBSERVATION]")

            print(
                f"Tool: {message.name}"
            )

            print(
                f"Result: {message.content}"
            )

    print("-" * 70)


def main():

    print_separator(
        "ReAct Agent with Custom Tools"
    )

    agent = create_agent()

    print("\nAgent loaded successfully!")

    print("\nAvailable tools:")
    print(" - calculate")
    print(" - define_word")
    print(" - get_current_datetime")

    print("\nThread ID: demo-session")

    print("\nType 'exit' to stop.")

    config = {
        "configurable": {
            "thread_id": "demo-session"
        }
    }

    while True:

        user_input = input("\nYou: ").strip()

        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        try:

            response = agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                },
                config=config
            )

            display_agent_response(response)

        except Exception as e:

            print("\nERROR:")
            print(e)


if __name__ == "__main__":
    main()