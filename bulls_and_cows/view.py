from abc import ABC, abstractmethod

class GameView(ABC):
    @abstractmethod
    def display_turn_start(self, turn: int):
        """
        Display the start of a new turn.
        """
        pass

    @abstractmethod
    def display_guess(self, guess: str):
        """
        Display the current guess.
        """
        pass

    @abstractmethod
    def display_response(self, response: str):
        """
        Display the response to the current guess.
        """
        pass

    @abstractmethod
    def display_congratulations(self, turns: int):
        """
        Display a congratulatory message when the game is won.
        """
        pass

class TextualView(GameView):
    def display_turn_start(self, turn: int):
        print(f"\nGuess {turn}")

    def display_guess(self, guess: str):
        print(guess)

    def display_response(self, response: str):
        print(response)

    def display_congratulations(self, turns: int):
        print(f"\nCongrats! You have won the game in {turns} turns!")
