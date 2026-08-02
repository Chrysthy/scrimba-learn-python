# cost = int("300")
# print(type(cost))

# service_charge = float("30")
# print(type(service_charge))

# print(cost + service_charge)


# budget = float(input("What is your budget for the project? "))
# print(budget)
# print(type(budget))


# Challenge: Build a simple paycheck calculator.
# 1. Instead of hard coded values, prompt the user for their hourly_rate and hours_worked.
# 2. Convert hourly_rate to a float and hours_worked to an integer.
# 3. Type check both variables.
# 4. Multiply them together and print the total pay.

hourly_rate = float(input("What's your hourly_rate? "))
hours_worked = int(input("How many hours did you work? "))

print(type(hourly_rate))
print(type(hours_worked))

print(hourly_rate * hours_worked)
