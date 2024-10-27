import argparse
from bulls_and_cows.game_controller import GameController

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Play the Bulls and Cows game.")
    parser.add_argument('--manual-guesser', action='store_true', help="Use manual guesser (default is automatic).")
    parser.add_argument('--manual-answerer', action='store_true', help="Use manual answerer (default is automatic).")
    args = parser.parse_args()

    gc = GameController(is_manual_answerer=args.manual_answerer, is_manual_guesser=args.manual_guesser)
    gc.play()