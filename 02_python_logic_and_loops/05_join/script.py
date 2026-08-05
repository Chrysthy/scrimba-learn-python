result = ", ".join(["peace", "love", "happiness"])
print(result)

result = " - ".join(["peace", "love", "happiness"])
print(result)

result = " AND ".join(["peace", "love", "happiness"])
print(result)

result = " ❤️ ".join(["peace", "love", "happiness"])
print(result)

result = "".join(["c", "a", "t"])
print(result)


# Challenge: Four Joiners

# 1. Join ["mysite.com", "products", "sale"] with "/" to build a URL path
# 2. Join ["2026", "05", "29"] with "-" to format a date
# 3. Join ["hip", "hip", "hooray"] with " " for the crowd
# 4. Join `letters` into a single word with no separator.

letters = ["p", "y", "t", "h", "o", "n"]

url = "/".join(["mysite.com", "products", "sale"])
date = "-".join(["2026", "05", "29"])
cheer = " ".join(["hip", "hip", "hooray"])
word = "".join(letters)

print(url)
print(date)
print(cheer)
print(word)