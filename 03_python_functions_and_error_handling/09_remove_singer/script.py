contacts = ["Freda", "Homer", "Chance"]
contacts.remove("Homer")

print(contacts)


def remove_contacts(contacts, name):

    for contact in contacts:

        if contact == name:
            contacts.remove(contact)

            print(f"Removed {name}.")

            return

    print(f"{name} isn't in your contacts.")

remove_contacts(contacts, "Homer")




queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def show_queue(queue):
  """Print everyone currently in the queue"""
  print()
  print("Current queue:")
  print()
  for singer in queue:
    name, song = singer
    print(f"{name} - {song}")
  print()
  print("Options:  add / remove / quit")

def prompt_for_singer():
  """Ask for a name and a song, and return them cleaned up."""
  name = input("Name: ").strip().title()
  song = input("Song: ").strip().title()
  return name, song

def add_singer(queue):
  """Ask for the singer and add them to the queue"""
  name, song = prompt_for_singer()
  queue.append((name, song))
  print()
  print(f"Added {name} to the queue.")

def remove_singer(queue): 
  """Remove singer fron the queue"""
  print("[remove a singer]")

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True 

    while is_running: 
      show_queue(queue)
      command = input("> ")

      if command == "quit": 
        is_running = False
        print("The queue is closed. Good night!")
      elif command == "add": 
        add_singer(queue)
      elif command == "remove":
        remove_singer(queue)
      else: 
        print(f"Sorry, I don't know the command '{command}'")

run_app(queue)
