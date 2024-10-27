import re
import random
from abc import ABC, abstractmethod
from .utils import ALL_WORDS
from bulls_and_cows.answerer import AutoAnswerer

class Guesser(ABC):
    @abstractmethod
    def get_guess(self, previous_response: str = None) -> str:
        """
        Get a guess from the player.
        """
        pass

    def is_valid(self, guess: str) -> bool:
        """
        Check if the guess is a valid word.
        """
        return guess in ALL_WORDS

class ManualGuesser(Guesser):
    def get_guess(self, _: str = None) -> str:
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
        self.__guess = None
        self.response_pattern = re.compile(r'(\d+)b(\d+)c')

    def get_guess(self, previous_response: str = None) -> str:
        """
        Automatically generate a guess by randomly selecting a word from the possible words.
        """
        if self.__guess and previous_response:
            self.__update_possible_words(previous_response)
        if not self.possible_words:
            raise ValueError("No possible words left to guess.")
        self.__guess = random.choice(self.possible_words)
        return self.__guess

    def __update_possible_words(self, response: str):
        """
        Update the list of possible words based on the response to the guess.
        """
        bulls, cows = self.__parse_response(response)
        self.possible_words = [
            word for word in self.possible_words
            if AutoAnswerer.calculate_bulls_and_cows(word, self.__guess) == (bulls, cows)
        ]

    def __parse_response(self, response: str) -> tuple:
        """
        Parse the response string to extract the number of bulls and cows.
        """
        match = self.response_pattern.match(response)
        if match:
            return tuple(map(int, match.groups()))
        else:
            raise ValueError("Invalid response format")