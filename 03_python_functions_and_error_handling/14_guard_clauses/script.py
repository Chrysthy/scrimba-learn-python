def serve_order(orders):
    if len(orders) == 0: # guard clause to prevent an error and check if the list is empty
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