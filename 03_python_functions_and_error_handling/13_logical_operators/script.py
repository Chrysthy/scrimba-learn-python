# 12 or over
# 140 or over
age = 11
height = 150

if age >= 12 and height >= 140: #True and True
    print("This person can ride.")
else:
    print("Sorry, not this time.")


if age >= 12 or height >= 140: #True or True
  print("This person can ride.")
else: 
  print("Sorry, not this time.")


logged_in = False
if not logged_in:
  print("Please log in.")


sold_out = ["Tuesday", "Saturday"]
day = "Wednesday"

if day not in sold_out: 
  print("Tickets are available!")