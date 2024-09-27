# Hangman Game in Python   


## Description

This is a simple console-based Hangman game implemented in Python. The player has to guess a randomly selected word by suggesting letters within a limited number of incorrect guesses. Each wrong guess results in a drawing of a hangman, progressing through stages until the player either guesses the word correctly or runs out of attempts.

### Features

- Word Selection: The game randomly selects a word from a predefined list, including hints for each word.
- User Interaction: Players input their letter guesses, with validation to ensure only single letters are accepted and that previously guessed letters are not counted again.
- Hangman Visualization: The game displays a hangman figure that progresses with each incorrect guess, providing a visual representation of the player's mistakes.
- Win/Loss Conditions: The game ends when the player correctly guesses the word or exceeds the maximum number of allowed mistakes.

### How to Play

1. Run the script in a Python environment.
2. Follow the prompts to enter letter guesses.
3. Aim to guess the word before making seven incorrect guesses.

### Requirements

- Python 3.x

### Getting Started

1. Clone this repository:
  
   git clone https://github.com/yourusername/hangman-game.git
   
2. Navigate to the project directory:
  
   cd hangman-game
   
3. Run the game:
  
   python hangman.py
   
### Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions are welcome!
