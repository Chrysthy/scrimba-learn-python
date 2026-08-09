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


