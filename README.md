# ReAct Agent with Custom Tools

This project demonstrates a LangGraph ReAct agent backed by Ollama. The agent can decide whether to answer directly or call one of three custom tools:

- `calculate`: safely evaluates arithmetic expressions using an allow-listed AST.
- `define_word`: looks up definitions in a small custom dictionary.
- `get_current_datetime`: returns the machine's current local date and time.

The agent uses `MemorySaver` as its checkpointer. Reusing the same `thread_id` preserves the conversation across turns; changing the thread starts a separate session.

## Run the interactive demo

Install the dependencies in the included virtual environment, make sure Ollama is running, and ensure the `llama3.2` model is available:

```text
ollama pull llama3.2
reactvenv\Scripts\activate
python main.py
```

Enter `exit` to stop. The console prints the ReAct trace, including the agent's tool decision, tool observation, and final answer.

## Run the five-question demonstration

```text
reactvenv\Scripts\activate
python -m tests.test_agent
```

Results are written to `outputs/test_results.txt`. The scenarios cover calculator and dictionary tools, two questions intended for direct answers, and a question that combines dictionary output with reasoning. Tool choices are recorded so you can compare the model's behavior with the intended ReAct routing. Run `python -m tests.test_memory` to demonstrate that facts persist across turns in one thread.
