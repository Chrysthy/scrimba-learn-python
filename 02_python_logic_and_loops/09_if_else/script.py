decibels = 90

if decibels > 89:
    print("Warning: Loud Environment!")
else:
    print("Noise levels acceptable.")


# Challenge: Quiz Pass or Fail
# You're building the results screen for an online course quiz. A student
# needs at least 60 points to pass.

# 1. Ask the student for their score and convert it to an int.
# 2. If their score is 60 or higher, print that they passed.
# 3. Otherwise, print that they didn't pass this time.

score = int(input("Enter your quiz score: "))

if score >= 60:
    print("Congrulations! You passed! Nice work.")
else:
    print("You didn't pass this time, please try again.")
