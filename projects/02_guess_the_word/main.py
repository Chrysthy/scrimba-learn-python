import random

print("Welcome to Guess the Word!")
print()
print("Unscramble the letters and discover the hidden tech word.")

words = ["burger", "video game", "cat"]

word = random.choice(words)

letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)

print(f"Scrambled: {scrambled_word}")

guess = input(
    f"type a guess or type 'skip' to skip the word: ").lower().strip()

if guess == "skip":
    print(f"Skipped! The word was {word}.")
elif guess == word:
    print("✅ Correct!")
else:
    print(f"❌ Sorry, the word was {word}.")