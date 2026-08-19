from agent import create_agent


def main():

    agent = create_agent()

    config = {
        "configurable": {
            "thread_id": "memory-demo"
        }
    }

    print("=" * 70)
    print("MEMORY TEST")
    print("=" * 70)

    # --------------------------------------------------
    # Turn 1
    # --------------------------------------------------

    response1 = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": (
                        "My name is Aninda and "
                        "I am learning AI engineering."
                    )
                }
            ]
        },
        config=config
    )

    print("\nTurn 1:")
    print(response1["messages"][-1].content)

    # --------------------------------------------------
    # Turn 2
    # --------------------------------------------------

    response2 = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is my name?"
                }
            ]
        },
        config=config
    )

    print("\nTurn 2:")
    print(response2["messages"][-1].content)

    # --------------------------------------------------
    # Turn 3
    # --------------------------------------------------

    response3 = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What am I learning?"
                }
            ]
        },
        config=config
    )

    print("\nTurn 3:")
    print(response3["messages"][-1].content)


if __name__ == "__main__":
    main()