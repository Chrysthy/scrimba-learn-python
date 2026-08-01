name = "Chrystine"
color = "purple"
restaurant = "Burger King"

about_me = f"My name is {name}, my favorite color is {color} and my favarite place to go is {restaurant}."

# Challenge: Excuse Generator

# Don't feel like going out tonight? Write a program that generates excuses for why you have to stay in.

# 1. Define these variables: first_name, event, number, noun, and verb. Use whatever values you want, as long as they match the format.
# 2. Write an f-string using your variables that generates a one-sentence excuse. Here's an example of what your output should look like:
#    "Sorry [Ted], I can't go to [the movies] — I have [345] [bees] to [crochet] and honestly it's taking longer than expected."
# 3. Print it! Change some or all of the values to create a new excuse. Print again.

first_name = "Noob"
event = "the party"
number = 200
noun = "pizzas"
verb = "eat"

excuse_generator = f"Sorry {first_name}, we can't go to {event} - We have {number} {noun} to {verb} together."

print(excuse_generator)
