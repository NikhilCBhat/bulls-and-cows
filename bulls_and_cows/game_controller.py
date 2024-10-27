from bulls_and_cows.guesser import AutoGuesser, ManualGuesser
from bulls_and_cows.answerer import AutoAnswerer, ManualAnswerer

class GameController:
    def __init__(self, is_manual_answerer: bool = True, is_manual_guesser: bool = True):
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
            print(f"\nGuess {turn}")
            guess = self.guesser.get_guess(self.response)
            print(guess)
            self.response = self.thinker.get_answer(guess)
            print(self.response)
            turn += 1
        print(f"\nCongrats! You have won the game in {turn - 1} turns!")

    def __is_game_over(self) -> bool:
        """
        Check if the game is over.
        """
        return self.response == "4b0c"