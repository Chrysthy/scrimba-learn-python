playlist = ["Bohemian Rhapsody", "Hey Jude", "Dancing Queen"]

print(playlist[0])
print(playlist[1])
print(playlist[2])
print(playlist[-1]) # último item da lista
print(playlist[10]) # error, index out of range

top_song = playlist[0]
print(f"Now playing: {top_song}")

# Challenge: Build a Support Queue
# You're building a help desk feature that shows who's waiting
# in line for support.

# Use indexing to print a status display that looks like this:
#
#   Now helping: Ada
#   Next in line: Grace
#   Just added: Alan
#
# "Now helping" is the first person in line, "Next in line" is second, and "Just added" is the last person in the queue.

tickets = ["Ada", "Grace", "Linus", "Margaret", "Alan"]

print(f"Now helping: {now_helping}")
print(f"Next in line: {next_in_line}")
print(f"Just added: {just_added}")

# print(f"Now helping: {tickets[0]}")
# print(f"Next in line: {tickets[1]}")
# print(f"Just added: {tickets[-1]}")
