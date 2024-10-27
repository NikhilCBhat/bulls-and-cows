from bulls_and_cows.guesser import AutoGuesser, ManualGuesser
from bulls_and_cows.answerer import AutoAnswerer, ManualAnswerer
from bulls_and_cows.view import TextualView

class GameController:
    def __init__(self, is_manual_answerer: bool = True, is_manual_guesser: bool = True):
        """
        Initialize the game controller with the specified modes.
        """
        self.guesser = ManualGuesser() if is_manual_guesser else AutoGuesser()
        self.thinker = ManualAnswerer() if is_manual_answerer else AutoAnswerer()
        self.response = None
        self.view = TextualView()

    def play(self):
        """
        Start the game loop.
        """
        turn = 1
        while not self.__is_game_over():
            self.view.display_turn_start(turn)
            guess = self.guesser.get_guess(self.response)
            self.view.display_guess(guess)
            self.response = self.thinker.get_answer(guess)
            self.view.display_response(self.response)
            turn += 1
        self.view.display_congratulations(turn - 1)

    def __is_game_over(self) -> bool:
        """
        Check if the game is over.
        """
        return self.response == "4b0c"