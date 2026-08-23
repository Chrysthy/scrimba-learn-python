def serve_order(orders):
    if len(orders) == 0:  # guard clause to prevent an error and check if the list is empty
        print("Nothing left to serve.")
        return

    item = orders.pop(0)
    print(f"Serving: {item}")


serve_order([])  # gives an error because the list is empty

orders = ["latte", "muffin"]
print(len(orders))


def fill_order(menu, order):
    if len(menu) == 0:
        print("Nothing available.")
        return

    if order not in menu:
        print(f"{order} isn't on the menu")
        return

# menu.remove(order)
# print(f"Order placed: {order}")


# Challenge: Call the Next Guest
# call_next() seats the first guest on a restaurant's waitlist. But when the waitlist is empty, the app crashes.
waitlist = []


def call_next(waitlist):
    """Seat the first guest on the waitlist."""
    name = waitlist[0]
    print(f"Now seating: {name}")

# 1. Add a guard clause to call_next() that exits early when the waitlist is empty,
#    and prints a message instead of crashing.
# 2. Test it with an empty waitlist to confirm it no longer crashes.


call_next(waitlist)
