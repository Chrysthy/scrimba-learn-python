number = int("42") # é uma string que representa um número inteiro. O int() consegue converter.
print(number)

number2 = int("banana") # error. Dá erro porque "banana" não pode ser convertido para um número inteiro, por isso ele gera um ValueError
print(number)

try:
    num = in("banana")
except ValueError:
    print("Please enter a number.")



try: 
    age = in(input("How old are you? "))
    print(f"You'll be {age + 1} next year.")
    
except ValueError:
    print("Please enter a number.")