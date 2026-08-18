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