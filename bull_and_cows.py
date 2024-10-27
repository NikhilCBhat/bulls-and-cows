import re
import random
import argparse
from abc import ABC, abstractmethod

def load_words(file_path):
    """
    Load words from the specified file path.
    """
    try:
        with open(file_path) as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        print("Word list file not found.")
        return set()

ALL_WORDS = load_words("4-letter-words-processed-new.txt")

class Guesser(ABC):
    @abstractmethod
    def get_guess(self) -> str:
        """
        Get a guess from the player.
        """
        pass

    def is_valid(self, guess) -> bool:
        """
        Check if the guess is a valid word.
        """
        return guess in ALL_WORDS

class Answerer(ABC):
    pattern = re.compile(r'^[0-4]b[0-4]c$')

    @abstractmethod
    def get_answer(self, guess) -> str:
        """
        Get the answer based on the guess.
        """
        pass

    def is_valid(self, answer) -> bool:
        """
        Check if the answer is in the correct format.
        """
        return bool(self.pattern.match(answer))

class AutoAnswerer(Answerer):
    def __init__(self, word=None) -> None:
        """
        Initialize with a secret word or choose one randomly.
        """
        self.__secret_word = word or random.choice(list(ALL_WORDS))

    def get_answer(self, guess) -> str:
        """
        Calculate the number of bulls and cows for the guess.
        """
        cows, bulls = 0, 0
        for i, c in enumerate(guess):
            if self.__secret_word[i] == c:
                bulls += 1
            elif c in self.__secret_word:
                cows += 1
        return f"{bulls}b{cows}c"

class ManualAnswerer(Answerer):
    def get_answer(self, guess) -> str:
        """
        Prompt the user for the answer.
        """
        while True:
            answer = input("What is the response? ").lower().strip()
            if self.is_valid(answer):
                return answer
            print("Answer is invalid. Must be in the format 3b1c")

class ManualGuesser(Guesser):
    def get_guess(self) -> str:
        """
        Prompt the user for a guess.
        """
        while True:
            guess = input("Enter your guess: ").upper().strip()
            if self.is_valid(guess):
                return guess
            print("Guess is invalid. Must be a 4 letter word")

class AutoGuesser(Guesser):
    def __init__(self):
        """
        Initialize the AutoGuesser with a list of possible words.
        """
        self.possible_words = list(ALL_WORDS)

    def get_guess(self) -> str:
        """
        Automatically generate a guess by randomly selecting a word from the possible words.
        """
        if not self.possible_words:
            raise ValueError("No possible words left to guess.")
        return random.choice(self.possible_words)

    def update_possible_words(self, guess, response):
        """
        Update the list of possible words based on the response to the guess.
        """
        bulls, cows = parse_response(response)
        self.possible_words = [
            word for word in self.possible_words
            if self._matches_response(word, guess, bulls, cows)
        ]

    def _matches_response(self, word, guess, bulls, cows):
        """
        Check if a word matches the given number of bulls and cows for a guess.
        """
        actual_bulls = sum(1 for i in range(len(word)) if word[i] == guess[i])
        actual_cows = sum(min(word.count(c), guess.count(c)) for c in set(guess)) - actual_bulls
        return actual_bulls == bulls and actual_cows == cows

def parse_response(response):
    """
    Parse the response string to extract the number of bulls and cows.
    """
    response_pattern = re.compile(r'(\d+)b(\d+)c')
    match = response_pattern.match(response)
    if match:
        return map(int, match.groups())
    else:
        raise ValueError("Invalid response format")

class GameController:
    def __init__(self, is_manual_answerer=True, is_manual_guesser=True):
        """
        Initialize the game controller with the specified modes.
        """
        self.guesser = ManualGuesser() if is_manual_guesser else AutoGuesser()
        self.thinker = ManualAnswerer() if is_manual_answerer else AutoAnswerer()
        self.response = None

    def play(self):
        """
        Start the game loop.
        """
        turn = 1
        while not self.__is_game_over():
            print(f"Guess {turn}")
            guess = self.guesser.get_guess()
            self.response = self.thinker.get_answer(guess)
            print(self.response)
            turn += 1
        print("Congrats! You have won the game!")

    def __is_game_over(self) -> bool:
        """
        Check if the game is over.
        """
        return self.response == "4b0c"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play the Bulls and Cows game.")
    parser.add_argument('--manual-guesser', action='store_true', help="Use manual guesser (default is automatic).")
    parser.add_argument('--manual-answerer', action='store_true', help="Use manual answerer (default is automatic).")
    args = parser.parse_args()

    gc = GameController(is_manual_answerer=args.manual_answerer, is_manual_guesser=args.manual_guesser)
    gc.play()