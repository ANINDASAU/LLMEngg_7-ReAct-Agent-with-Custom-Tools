from langchain_core.tools import tool


DEFINITIONS = {
    "artificial intelligence": (
        "Artificial Intelligence is the field of computer science "
        "that focuses on creating systems capable of performing tasks "
        "that normally require human intelligence."
    ),

    "machine learning": (
        "Machine Learning is a branch of artificial intelligence "
        "where computers learn patterns from data and use those "
        "patterns to make predictions or decisions."
    ),

    "photosynthesis": (
        "Photosynthesis is the process by which green plants use "
        "sunlight, carbon dioxide, and water to produce glucose and oxygen."
    ),

    "neural network": (
        "A neural network is a machine learning model inspired by "
        "the structure of the human brain, consisting of interconnected "
        "nodes arranged in layers."
    ),

    "deep learning": (
        "Deep learning is a type of machine learning that uses "
        "multi-layer neural networks to learn complex patterns from data."
    ),

    "python": (
        "Python is a high-level programming language widely used "
        "in software development, data science, machine learning, "
        "and artificial intelligence."
    ),
}


@tool
def define_word(word: str) -> str:
    """
    Return a definition from the custom dictionary.
    Use only when the user explicitly asks what a word or concept means.
    """

    word = word.lower().strip()

    definition = DEFINITIONS.get(word)

    if definition:
        return definition

    return (
        f"No definition is available in the custom dictionary "
        f"for '{word}'."
    )