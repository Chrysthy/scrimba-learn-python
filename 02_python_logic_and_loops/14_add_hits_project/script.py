# Challenge: Let the Player Ask for a Hint
# The word_bank below pairs each word with a hint. Wire up a 'hint' option
# so a stuck player can reveal the clue and then keep guessing.

# 1. Pick a random pair from word_bank and unpack it into word and hint.
# 2. Update the guess prompt so the player knows 'hint' is now an option.
# 3. If the player types 'hint', show them the hint, then ask them to guess again.
#    * Hint: this will require adding a second input prompt!
#    * Hint: keep the 'hint' check in its own separate if, above the
#      skip/correct/wrong block. Skip, correct, and wrong all end the turn,
#      but a hint doesn't. Keeping it separate lets the game show the hint
#      and then still check the guess the player types next.
# 4. Optional: add a couple of your own word/hint pairs to the bank.

import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

word, hint = random.choice(word_bank)

letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters).upper()

print(f"Scrambled: {scrambled_word}")

guess = input("Guess the word (or type 'hint' / 'skip'): ").strip().lower()


if guess == "hint":
    print()
    print(f"Hint: {hint}")
    print()
    guess = input("Your guess (or 'skip'): ").strip().lower()


if guess == "skip":
  print(f"Skipped! The word was '{word}'.")
elif guess == word:
  print("✅  Correct!")
else:
    print(f"❌ Sorry, the word was '{word}'.")