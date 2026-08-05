letters = list("listen")

print(letters)
print(sorted(letters))

first_word = list("listen")
second_word = list("silent")

print(sorted(first_word))
print(sorted(second_word))

# Challenge: Anagram Check
# Anagrams are two words made from the exact same letters rearranged,
# like "listen" and "silent".

# For each pair below, split both words into lists, sort them, and print
# the results. If the two lists match, the words are anagrams.

# 1. "earth" and "heart"
# 2. "below" and "elbow"
# 3. "night" and "tight"

earth = list("earth")
heart = list("heart")

print(sorted(earth))
print(sorted(heart))


below = list("below") 
elbow = list("elbow")

print(sorted(below))
print(sorted(elbow))


night = list("night")
tight = list("tight")

print(sorted(night))
print(sorted(tight))
