# BINGO!
bingo_numbers = ["B-7", "I-22", "N-33", "G-51", "O-68", "B-3", "I-19", "O-72"]
already_called = ["B-7", "I-22", "G-51"]

print("B-7" in already_called)
print("O-68" in already_called)


import random

pick = random.choice(bingo_numbers)

while pick in already_called:
  pick = random.choice(bingo_numbers)


print(f"Next call: {pick}")

already_called.append(pick)

print(already_called)