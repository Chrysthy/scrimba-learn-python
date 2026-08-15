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