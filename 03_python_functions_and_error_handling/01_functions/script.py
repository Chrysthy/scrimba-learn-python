import random

# roll = random.randint(1,6)
# print(f"You rolled a {roll}")

# def = significa definir uma função - define
def roll_dice():
    roll = random.randint(1,6)
    print(f"You rolled a {roll}")

roll_dice()
roll_dice()
roll_dice()

# função que chama outra função
def throw_dice():
  roll_dice()
  roll_dice()

throw_dice()

def show_welcome():
   print()
   print("Welcome to Dice Fight!")
   print()

# A função play_game chama as funções show_welcome e throw_dice e executa o jogo
def play_game():
   show_welcome()
   throw_dice()

play_game()

# Challenge: Write some functions!
# You've very generously decided to pick up coffee for six of your favorite coworkers this morning. 

# 1. Write a function announcing your coffee run. 
# Example output: "I am headed to the coffee shop! Who wants a latte?"

# 2. Write a function to calculate the total cost if you buy them each a latte for $5. In an f string, print how many lattes and what the total comes to.  
# Example output: 
# 6 lattes comes to $30.

# 3. Your coworkers thank you profusely. To save a little time, write a function that prints "You're welcome!" twice, then call it as many times as you need to thank all six coworkers. 

# 4. Put all your function calls in a new function called coffee_run(), and call it to start your coffee run!