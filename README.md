# Bulls and Cows Game

```
         (__)
         (oo)
  /-------\/
 / |     ||
*  ||----||
   ^^    ^^
```

Welcome to the Bulls and Cows game! This is a classic code-breaking game where the player tries to guess a four-letter secret word, and the game provides feedback in terms of "bulls" and "cows."

## Game Overview

- **Bulls**: The number of letters in your guess that are in the correct position.
- **Cows**: The number of letters in your guess that are in the word but in the wrong position.

The objective is to guess the secret word with the correct number of bulls and cows.

### How to Play

1. **Start the Game**: Run the game using the instructions in the "Usage" section below.
2. **Make a Guess**: Enter a four-letter word as your guess.
3. **Receive Feedback**: After each guess, you'll receive feedback in the form of "bulls" and "cows."
   - Example: If the secret word is "game" and you guess "gale," you will receive feedback of "2b1c" (2 bulls, 1 cow) because 'g' and 'a' are in the correct positions (bulls), and 'e' is in the word but in the wrong position (cow).
4. **Continue Guessing**: Use the feedback to refine your guesses until you guess the word correctly with 4 bulls.

## Features

- Play against the computer or manually input responses.
- Automatic guessing by the computer.
- Configurable to switch between manual and automatic modes.
- Supports both manual and automatic answerers.
- Modular view system to separate game logic from display logic.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bulls-and-cows.git
   cd bulls-and-cows
   ```

2. **Ensure you have Python 3 installed**.

## Usage

1. **Prepare the word list**:
   - Ensure you have a file named `4-letter-words.txt` in the root directory. This file should contain a list of valid 4-letter words, one per line.

2. **Run the game**:
   ```bash
   python game.py
   ```

3. **Game Modes**:
   - **Mode 1: Guess the Word!** The computer thinks of a word, and you play against it by entering guesses.
     - Command: `python game.py --manual-guesser`
   - **Mode 2: Stump the Computer!** You think of a word, and answer while the computer guesses.
     - Command: `python game.py --manual-answerer`
   - **Mode 3: Pass and Play!** You and your friend can answer/guess side by side.
     - Command: `python game.py --manual-guesser --manual-answerer`
   - **Mode 4: Spectate!** Watch the computer play the game :)
     - Command: `python game.py`

## Code Structure

- **`bulls_and_cows/`**: Contains the main modules for the game.
  - **`game_controller.py`**: Manages the game flow and interactions between guessers and answerers.
  - **`guesser.py`**: Contains the `Guesser`, `ManualGuesser`, and `AutoGuesser` classes.
  - **`answerer.py`**: Contains the `Answerer`, `ManualAnswerer`, and `AutoAnswerer` classes.
  - **`view.py`**: Contains the `GameView`, and `TextualView` class for displaying game information.
  - **`utils.py`**: Contains utility functions like `load_words` and `parse_response`.

- **`4-letter-words.txt`**: The word list file.

- **`game.py`**: The main script to run the game.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.