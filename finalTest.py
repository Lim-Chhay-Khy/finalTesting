"""Simple lesson demo for reading Python code and using functions."""

LETTER_POINTS = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}


def num_points(word):
    """Return the total score for a word."""
    total = 0
    for letter in word.lower():
        total += LETTER_POINTS.get(letter, 0)
    return total


def best_word(word_list):
    """
    word_list is a list of words.

    Return the word worth the most points.
    """
    current_best_word = ""
    best_points = 0

    for word in word_list:
        points = num_points(word)
        if points > best_points:
            current_best_word = word
            best_points = points

    return current_best_word


def explain_best_word():
    """Print a simple explanation of how the function works."""
    print("\nHow to read the best_word function:")
    print("1. Start with an empty best word and 0 points.")
    print("2. Go through each word in the list.")
    print("3. Use num_points(word) to score that word.")
    print("4. If the score is higher than the current best score, update both values.")
    print("5. Return the word with the highest score at the end.")


def demo_built_in_functions():
    """Show examples of Python built-in functions."""
    print("\nBuilt-in function examples:")
    print("max(4, 10, 2) =", max(4, 10, 2))
    print("print() sends a message to the screen.")


def get_words_from_user():
    """Ask the user for words and return them as a list."""
    response = input("\nEnter some words separated by spaces: ").strip()
    if not response:
        return ["cat", "zebra", "apple", "quiz"]
    return response.split()


def show_word_scores(words):
    """Display the score for each word."""
    print("\nWord scores:")
    for word in words:
        print(f"{word}: {num_points(word)} points")


def main():
    """Run the lesson demo."""
    print("Reading Python Code Demo")
    print("This program shows how functions break a problem into smaller parts.")

    words = get_words_from_user()
    show_word_scores(words)

    top_word = best_word(words)
    print(f"\nBest word: {top_word}")
    print(f"Best word score: {num_points(top_word)}")

    explain_best_word()
    demo_built_in_functions()


if __name__ == "__main__":
    main()
