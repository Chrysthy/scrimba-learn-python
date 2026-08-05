import random

lunch_spots = ["Thai Palace", "Burrito Bar", "Noodle House"]

print(random.choice(lunch_spots))

random.shuffle(lunch_spots) # muda a lista 
print(lunch_spots)

print(sorted(lunch_spots)) # cria uma cópia e a lista original fica intacta
print(lunch_spots)


# Challenge: Turn Order
# You're building a feature for a board game app that sets up each match.
# At the start of a game, you need to put the players in a random turn
# order, and also randomly choose one player to deal the cards.

# 1. Shuffle the players into a random turn order, then print the list.
# 2. Randomly choose one player to be the dealer and print:
#    "<name> deals first"

players = ["Mara", "Devon", "Priya", "Leo"]

random.shuffle(players)
print(players)

card_dealer = random.choice(players)
print(f"{card_dealer} deals first")
#print(f"{random.choice(players)} deals first")