import random

# Challenge: Scramble a Word
# 1. Create a game file named `jargon_jumble.py`
# 2. Create a list of at least 3 words and save to a variable called `words`
# 3. Use random.choice() to pick a word from the list
# 4. Use list(), random.shuffle(), and "".join() to scramble the word
# 5. Print the scrambled word

words = ["burger", "video game", "cat"]

word = random.choice(words)
print(word)

letters = list(word)
random.shuffle(letters)
scrambled_word = "".join(letters)

print(f"Scrambled: {scrambled_word}")