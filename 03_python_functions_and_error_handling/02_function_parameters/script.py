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