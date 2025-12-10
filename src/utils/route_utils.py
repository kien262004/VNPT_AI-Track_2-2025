def count_word(text: str) -> int:
    """Count the number of words in a given text."""
    words = text.split()
    return len(words)