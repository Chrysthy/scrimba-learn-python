breakfast = "pancakes "
lunch = "salad "
dinner = "pizza"

# meal_plan = breakfast + " " + lunch + " " + dinner or meal_plan = f"{breakfast} {lunch} {dinner}"
meal_plan = breakfast + lunch + dinner
print(meal_plan)

# Challenge - Daily Planner
# Print a sentence that outlines your plan for today.

# 1. Make three variables: morning, afternoon, and evening.
# 2. To each variable, save a string containing one activity (taking a nap, skiing, etc).
# 3. Add each variable together and save to a variable called `plan_for_today`

# Here's an example of what your output should look like:
# "My plan for today day is: 1. drink coffee 2. study Python 3. dance party"
# Hint: There's no magic to numbering the list, just include them in your strings!

morning = "1. Take a morning walk "
afternoon = "2. Play video games"
evening = "3. Read a book"

plan_for_today = f"My plan for today is: {morning} {afternoon} {evening}"

print(plan_for_today)
