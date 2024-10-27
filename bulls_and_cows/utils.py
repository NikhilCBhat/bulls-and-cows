def __load_words(file_path: str) -> set:
    """
    Load words from the specified file path.
    """
    try:
        with open(file_path) as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        print("Word list file not found.")
        return set()

ALL_WORDS = __load_words("4-letter-words.txt")
