print("Welcome to PayUp")

meal_type = input("What type of meal was it? (e.g. lunch, dinner, brunch): ")

event_name = input("What is the name of the event or occasion? ")

cost = float(input(
    "What is the cost of the event? Enter a whole number (e.g. 300 for $300): "))

service_charge = int(input(
    "Was there a tip or a service charge? Enter a whole number (e.g. 20 for 20%): ").strip("%"))

group_size = int(input("How many people are splitting the bill? "))

service_charge_total = cost * service_charge / 100

grand_total = cost + service_charge_total

total_per_person = grand_total / group_size

print()
print(f"Here's the breakdown for {meal_type} at {event_name}:")
print()
print(f"Cost: ${cost:.2f}")
print(f"Service charges: ${service_charge_total:.2f}")
print(f"Group size: {group_size}")
print(f"Grand total: ${grand_total:.2f}")
print()
print(f"Each person must PayUP: ${total_per_person:.2f}")
