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

## Example

```text
Welcome to ByteShuffle!

Unscramble the letters and discover the hidden tech word.

Round 1 of 5

Scrambled: XATNSY

Guess the word (or type 'hint' / 'skip' / 'quit'): hint

Hint: One missing bracket, and Python hits me with a ____ error.

Your guess (or 'skip' / 'quit'): syntax

✅ Correct!
```

After five rounds:

```text
Final score: 4/5

🎉 Near perfect, only one failing test!
```

## Concepts Practiced

- Variables
- Lists and tuples
- While loops
- Conditional statements
- User input
- String methods
- Random selection
- Shuffling lists
- Membership checks
- Counters
- Score tracking
- F-strings

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Chrysthy/scrimba-learn-python.git
```

2. Open the project directory:

```bash
cd scrimba-learn-python/projects/02_word_scramble_game
```

3. Run the Python file:

```bash
python main.py
```