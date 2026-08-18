import math

def slices_needed(guests):
    return guests * 2

slices_needed(10)


def pizzas_needed(slices):
   return math.ceil(slices / 8)


silces = slices_needed(10)
pizzas = pizzas_needed(slices)

print(pizzas)

# diferença entre print e return
# print mostra o valor na tela, no terminal
# return retorna o valor para o código para que você possa salvar e usar





# Challenge: Returning functions 
# For each function, save the result to a variable, then use the result to print an f string.

# 1. Write room_area(length, width) that returns the area of a room. Get the area of a
#    12 by 10 room.
#    Example output:
#    The room is 120 square feet.

# 2. Write add_tax(price) that returns a price with 8% tax added (multiply by 1.08). Get
#    the total for a $50 item.
#    Example output:
#    With tax, that comes to $54.0.

# 3. Write full_name(first, last) that returns a first and last name joined with a space.
#    Use it to build a name, then print a greeting with it.
#    Example output:
#    Welcome, Mike Reed!


def room_area(length, width):
   return length * width

area = room_area(12, 10)

print(f"The room is {area} square feet.")



