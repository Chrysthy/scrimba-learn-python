def greet_jenny():
  print("Welome, Jenny!")

def greet_marcus():
  print("Welcome, Marcus!")


# você define uma função com um parâmetro e você pode passar vários parâmetros
# os parâmetros são como suas variáveis
# local scope
def great(name, unread_messages ):
    print(f"Welcome, {name}!")
    print(f"Welcome, {name}! You have {unread_messages} new messages.")


# quando você chama a função, passa o argumento
# argumentos são os valores que você está colocando nas variáveis
greet("Jenny")
greet("Marcus")
greet("Mary", 15)
greet("Sam", 100+)


# global scope
def show_welcome(): 
  print(f"Welcome to {shop_name}")

show_welcome()



# Challenge: Write two functions with parameters
# Write each function underneath its instructions, then call it with the values given.

# 1. Write a function called add_numbers that prints the sum of the two numbers you pass in.
#    Call it a couple of times with different numbers.
#    Example output:
#    add_numbers(2, 3) prints 5
#    add_numbers(10, 45) prints 55


# 2. You've scrambled a word before: turn it into a list of letters, shuffle them, and
#    join them back together. Let's make that reusable. Write scramble(word) so it takes
#    any word and prints a scrambled version of it.
#    Example output:
#    scramble("python") might print nohtyp