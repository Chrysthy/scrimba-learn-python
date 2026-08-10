#4682B4
steel_blue = (70, 130, 180)

print(steel_blue[0])

# steel_blue[0] = 300 
# print(steel_blue[0]) não é possível alterar o valor de uma tupla, pois ela é imutável.

#unpacking 
red, green, blue = steel_blue
print(red)
print(green)
print(blue)


color_palette = [
  (70, 130, 180),
  (240, 128, 128),
  (60, 179, 113)
]

print(color_palette[0])

red, green, blue = color_palette[0]
print(f"RGB: {red}, {green}, {blue}")

red, green, blue = color_palette[1]
print(f"RGB: {red}, {green}, {blue}")


# Challenge: Inventory Check
# Build an inventory display feature for a small office supply store.
# 1. Unpack the item and quantity for each entry in the list of tuples.
# 2. Print each item and it's quantity in this format: "notebooks: 42 in stock"

inventory = [
    ("notebooks", 42),
    ("pens", 130),
    ("staplers", 8),
]

item, quantity = inventory[0]
print(f"{item}: {quantity} in stock")

item, quantity = inventory[1]
print(f"{item}: {quantity} in stock")

item, quantity = inventory[2]
print(f"{item}: {quantity} in stock")