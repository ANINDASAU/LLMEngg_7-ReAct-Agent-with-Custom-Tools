from pathlib import Path
from agent import create_agent


OUTPUT_FILE = Path("outputs/test_results.txt")


def run_test(agent, question, thread_id):

    config = {
        "configurable": {
            "thread_id": thread_id
        }
    }

    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ]
        },
        config=config
    )

    messages = response["messages"]
    tool_calls = [
        message
        for message in messages
        if type(message).__name__ == "AIMessage"
        and getattr(message, "tool_calls", None)
    ]
    observations = [
        message
        for message in messages
        if type(message).__name__ == "ToolMessage"
    ]

    return {
        "answer": messages[-1].content,
        "actions": [
            call["name"]
            for message in tool_calls
            for call in message.tool_calls
        ],
        "observations": [message.content for message in observations],
    }


def main():

    agent = create_agent()

    tests = [
        (
            "Calculator",
            "What is 245 * 36?"
        ),
        (
            "Dictionary",
            "What does photosynthesis mean?"
        ),
        (
            "Direct Answer 1",
            "Write a one-sentence greeting for a student learning programming."
        ),
        (
            "Direct Answer 2",
            "Explain in one sentence why regular practice improves skills."
        ),
        (
            "Combined Reasoning",
            "What does photosynthesis mean, and why is it important for life?"
        ),
    ]

    output_lines = []

    output_lines.append("=" * 70)
    output_lines.append("REACT AGENT TEST RESULTS")
    output_lines.append("=" * 70)

    for index, (name, question) in enumerate(tests, start=1):

        result = run_test(
            agent,
            question,
            f"test-{index}"
        )

        output_lines.append("")
        output_lines.append(f"TEST {index}: {name}")
        output_lines.append("-" * 70)
        output_lines.append(f"Question: {question}")
        output_lines.append(
            f"Actions: {', '.join(result['actions']) or 'No tool call'}"
        )
        for observation in result["observations"]:
            output_lines.append(f"Observation: {observation}")
        output_lines.append(f"Answer: {result['answer']}")

        print(f"\nTEST {index}: {name}")
        print(f"Question: {question}")
        print(
            f"Actions: {', '.join(result['actions']) or 'No tool call'}"
        )
        print(f"Answer: {result['answer']}")

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    OUTPUT_FILE.write_text(
        "\n".join(output_lines),
        encoding="utf-8"
    )

    print("\n" + "=" * 70)
    print(f"Results saved to: {OUTPUT_FILE}")
    print("=" * 70)


if __name__ == "__main__":
    main()