# print(20 + 10) 30
# print(20 - 10) 10
# print(20 / 10) 2.0
# print(20 * 10) 200

current_ties = 15
new_ties = 3
total_ties = current_ties + new_ties
print(total_ties)

total_cost = 5 * new_ties
print(total_cost)

remaining_ties = total_ties - 10
print(remaining_ties)

ties_per_friend = remaining_ties / 4
print(ties_per_friend)

print(f"I have {current_ties + new_ties} ties in my collection.")


# Challenge: Practice arithmetic operators
# - Save each value to a variable
# - Do the calculation and save to another variable
# - Print the result!

# 1. You have 200 songs in your library. You delete 47. Print how many are left.
# 2. A movie ticket costs $12. You're buying for yourself and 2 friends. Print the total cost.
# 3. You have 48 stickers to share equally among 6 friends. Print how many each person gets.

my_songs = 200
deleted_songs = 47
new_total_songs = my_songs - deleted_songs
print(new_total_songs)

movie_ticket_cost = 12
num_of_tickets = 3
total_tickets = movie_ticket_cost * num_of_tickets
print(total_tickets)

stickers = 48
friends = 6
stickers_per_friend = stickers / friends
print(stickers_per_friend)
