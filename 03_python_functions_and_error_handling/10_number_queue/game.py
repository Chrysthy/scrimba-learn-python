queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

# Challenge: 
# 1. Update show_queue() so the list is always numbered.
# 2. Print each singer with their number, starting at 1 (hint: you can do math inside of an f string).
# 3. Try adding and removing several singers from the list to make sure the numbering stays consistent. 

# Example output:
#
# Current Queue:
#
# 1. Annie - Dancing Queen
# 2. Allen - Country Roads
#
# Options: add / remove / quit

def show_queue(queue):
  """Print everyone currently in the queue"""
  print()
  print("Current queue:")
  print()
  for i, singer in enumerate(queue):
    name, song = singer
    print(f"{i + 1}. {name} - {song}")
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
  name = input("Who do you want to remove? ").strip().title()
  print()
  for singer in queue:
    if singer[0] == name:
      queue.remove(singer)
      print(f"Removed {name} from the queue.")
      return 
  print(f"There's no one named {name} in the queue.")


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
