# Bulls and Cows Game

Welcome to the Bulls and Cows game! This is a classic code-breaking game where the player tries to guess a secret word, and the game provides feedback in terms of "bulls" and "cows."

## Game Overview

- **Bulls**: The number of letters in your guess that are in the correct position.
- **Cows**: The number of letters in your guess that are in the word but in the wrong position.

The objective is to guess the secret word with the correct number of bulls and cows.

## Features

- Play against the computer or manually input responses.
- Automatic guessing by the computer.
- Configurable to switch between manual and automatic modes.
- Supports both manual and automatic answerers.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bulls-and-cows.git
   cd bulls-and-cows
   ```plaintext

2. **Ensure you have Python 3 installed**.

## Usage

1. **Prepare the word list**:
   - Ensure you have a file named `4-letter-words-processed-new.txt` in the root directory. This file should contain a list of valid 4-letter words, one per line.

2. **Run the game**:
   ```bash
   python game.py
   ```plaintext

3. **Game Modes**:
   - **Manual Guesser**: You enter guesses manually.
   - **Auto Guesser**: The computer generates guesses automatically.
   - **Manual Answerer**: You provide feedback manually.
   - **Auto Answerer**: The computer provides feedback automatically.

4. **Switching Modes**:
   - You can switch between manual and automatic modes using command-line arguments:
     - `--manual-guesser`: Use manual guesser (default is automatic).
     - `--manual-answerer`: Use manual answerer (default is automatic).

   Example:
   ```bash
   python game.py --manual-guesser --manual-answerer
   ```plaintext

## Code Structure

- **`bulls_and_cows/`**: Contains the main modules for the game.
  - **`game_controller.py`**: Manages the game flow and interactions between guessers and answerers.
  - **`guesser.py`**: Contains the `Guesser`, `ManualGuesser`, and `AutoGuesser` classes.
  - **`answerer.py`**: Contains the `Answerer`, `ManualAnswerer`, and `AutoAnswerer` classes.
  - **`utils.py`**: Contains utility functions like `load_words` and `parse_response`.

- **`4-letter-words.txt`**: The word list file.

- **`game.py`**: The main script to run the game.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.