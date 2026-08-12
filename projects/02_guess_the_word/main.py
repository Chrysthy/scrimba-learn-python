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


print("Welcome to Guess the Word!")
print()
print("Unscramble the letters and discover the hidden tech word.")

ROUNDS = 5
round_num = 1

used = []

while ROUNDS <= 5:

    word, hint = random.choice(word_bank)

    while (word, hint) in used:
        word, hint = random.choice(word_bank)

    used.append((word, hint))

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).upper()


    print()
    print(f"Round {round_num} of {ROUNDS}")
    print()
    print(f"Scrambled: {scrambled_word}")
    print()

    guess = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()

   
    if guess == "hint":
        print()
        print(f"Hint: {hint}")
        print()
        guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()


    if guess == "quit":
        print("Thanks for playing! See you later!")
        break

    elif guess == "skip":
        print(f"Skipped! The word was '{word}'.")
    elif guess == word:
        print("✅  Correct!")
    else:
        print(f"❌ Sorry, the word was '{word}'.")

    round_num += 1