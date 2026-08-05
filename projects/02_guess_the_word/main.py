print("Welcome to Guess the Word!")
print()
print("Unscramble the letters and discover the hidden tech word.")

words = ["burger", "video game", "cat"]

word = random.choice(words)
print(word)

letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)

print(f"Scrambled: {scrambled_word}")