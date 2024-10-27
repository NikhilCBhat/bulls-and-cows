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
   - You can switch between manual and automatic modes by modifying the `GameController` initialization in `bulls_and_cows.py`.

## Code Structure

- **Guesser**: Abstract base class for guessers.
- **Answerer**: Abstract base class for answerers.
- **ManualGuesser**: Class for manual guessing.
- **AutoGuesser**: Class for automatic guessing.
- **ManualAnswerer**: Class for manual answering.
- **AutoAnswerer**: Class for automatic answering.
- **GameController**: Manages the game flow and interactions between guessers and answerers.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.