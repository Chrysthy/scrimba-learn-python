# meal_total = 100
# tip = 15
# print(meal_total + tip)

# grand_total = meal_total + tip
# print(grand_total)


# Challenge

# 1. You and your friends just had dinner. Save the cost of the food to a variable called food_total.
# 2. Save the cost of the drinks to a separate variable called drinks_total.
# 3. Add them together and save the result to a variable called meal_total.
# 4. Print meal_total.
# 5. One friend didn't drink. Reduce drinks_total by whatever amount makes sense,
#    and print meal_total again. Did it update?


food_total = 85
drinks_total = 30
meal_total = food_total + drinks_total

print(meal_total)

drinks_total = 15
print(meal_total)  # This will still print the original meal_total because we haven't updated it after changing drinks_total.

meal_total = food_total + drinks_total # Update the meal_total with the new drinks_total.
print(meal_total) # This will print the updated meal_total after reducing drinks_total.