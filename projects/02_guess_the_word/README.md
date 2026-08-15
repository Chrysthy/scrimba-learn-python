<h1 align="center"> Guess the Word </h1>

<p align="center">Guess the Word is a Python command-line game where players unscramble tech-related words, use hints when needed, and try to get the highest score in five rounds.</p>

## Demo

![ByteShuffle Demo](./assets/gif-do-projeto.gif)

## How It Works

The game randomly selects tech-related words and scrambles their letters. The player has five rounds to figure out the correct word and can request a hint, skip a round, or quit the game.

For each round, the application:

- Randomly selects a word from the word bank
- Makes sure the same word is not used twice
- Shuffles the letters
- Displays the scrambled word
- Asks the player to guess the original word
- Updates the score after a correct answer

The player can also type:

- `hint` to reveal a sentence with a clue
- `skip` to skip the current word
- `quit` to leave the game

At the end, the game displays the final score along with a message based on the player's result.
