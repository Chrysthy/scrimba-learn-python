# Challenge: Create the output display for the PayUp app.

# 1. Check out the example output in `example_output.md`
# 2. Define a variable for each item: event name, cost, service charge,
#    group size, grand total, and total per person. Use made-up values for now —
#    we'll do the math later!
# 3. Build the display line by line using print() and f-strings. 
#    Remember: an empty print() creates a blank line.
# 4. Run it and make sure it matches the example.

meal_type = "dinner"
event_name = "Party"
cost = 300
service_charge = 20
group_size = 4
grand_total = cost + service_charge
total_per_person = grand_total / group_size

print("Welcome to PayUp")
print()
print(f"Here's the breakdown for {meal_type} at {event_name}:")
print()
print(f"Cost: ${cost}")
print(f"Service charges: ${service_charge}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total}")
print()
print(f"Each person must PayUP: {total_per_person}")