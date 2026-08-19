from langgraph.checkpoint.memory import MemorySaver


def create_memory() -> MemorySaver:
	"""Create the in-memory checkpointer used for conversation threads."""

	return MemorySaver()
