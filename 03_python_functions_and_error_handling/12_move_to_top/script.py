tasks = ["do laundry", "call mom"]

tasks.insert(0, "pay rent")
print(tasks)  # Output: ['pay rent', 'do laundry', 'call mom']

todo = tasks.pop(2)
tasks.insert(0, todo)
print(tasks)

