contacts = ["Freda", "Homer", "Chance", "Lisa"]
contacts.remove("Homer")

print(contacts)


def remove_contacts(contacts, name):

    for contact in contacts:

        if contact == name:
            contacts.remove(contact)

            print(f"Removed {name}.")

            return

    print(f"{name} isn't in your contacts.")


remove_contacts(contacts, "Chance")
print(contacts)

