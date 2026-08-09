# Challenge: Check if the Guess Is Correct
# Add interactivity so a player
# can either a) skip the word and get the correct answer or b) guess the word and find out if they're correct.

# 1. Prompt the player for input and give them two options: type a guess or type 'skip' to skip the word.
# 2. Use string methods to clean the player's guess and improve the display:
#    - We want to be as forgiving as we can with the player's guess. Clean the player's guess so that capitalization and white space don't matter when comparing to the correct answer.
#    - Display the scrambled word in all caps so it stands out on screen.
# 3. Use if/elif/else to handle three cases:
#    - Player types "skip": Skipped! The word was 'apple'.
#    - Player's guess is correct: ✅ Correct!
#    - Player's guess is incorrect: ❌ Sorry, the word was 'apple'.

import random

words = ["apple", "orange", "banana"]

word = random.choice(words)
print(word)
letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters).upper()

print(f"Scrambled: {scrambled_word}")

guess = input(
    f"type a guess or type 'skip' to skip the word: {scrambled_word} ").lower().strip()


if guess == "skip":
    print(f"Skipped! The word was {word}.")
elif guess == word:
    print("✅ Correct!")
else:
    print(f"❌ Sorry, the word was {word}.")
