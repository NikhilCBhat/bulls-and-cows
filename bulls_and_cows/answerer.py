import random
import re
from abc import ABC, abstractmethod
from .utils import ALL_WORDS

class Answerer(ABC):
    pattern = re.compile(r'^[0-4]b[0-4]c$')

    @abstractmethod
    def get_answer(self, guess: str) -> str:
        """
        Get the answer based on the guess.
        """
        pass

    def is_valid(self, answer: str) -> bool:
        """
        Check if the answer is in the correct format.
        """
        return bool(self.pattern.match(answer))

class AutoAnswerer(Answerer):
    def __init__(self, word: str = None) -> None:
        """
        Initialize with a secret word or choose one randomly.
        """
        self.__secret_word = word or random.choice(list(ALL_WORDS))

    def get_answer(self, guess: str) -> str:
        """
        Calculate the number of bulls and cows for the guess.
        """
        bulls, cows = self.calculate_bulls_and_cows(guess, self.__secret_word)
        return f"{bulls}b{cows}c"

    @staticmethod
    def calculate_bulls_and_cows(guess: str, secret_word: str) -> tuple:
        """
        Calculate bulls and cows for a given guess and secret word.
        """
        bulls = sum(1 for x, y in zip(guess, secret_word) if x == y)
        cows = sum(min(secret_word.count(c), guess.count(c)) for c in set(guess)) - bulls
        return bulls, cows

class ManualAnswerer(Answerer):
    def get_answer(self, _: str) -> str:
        """
        Prompt the user for the answer.
        """
        while True:
            answer = input("What is the response? ").lower().strip()
            if self.is_valid(answer):
                return answer
            print("Answer is invalid. Must be in the format 3b1c")