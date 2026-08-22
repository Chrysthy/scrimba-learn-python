queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]


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

    name = input("Name: ").strip().title()
    song = input("Song: ").strip().title()

    return name, song


def add_singer(queue):

    name, song = prompt_for_singer()
    print(name, song)

    queue.append((name, song))
    print()
    print(f"Aded {name} to the queue")


def remove_singer(queue):
    """Remove singer fron the queue"""
    name = input("Who do you want to remove?").strip().title()
    print()

    for singer in queue:
        if singer[0] == name:
            queue.remove(singer)

            print(f"Removed {name} from the queue")
            return

    print(f"There's no one named {name} in the queue.")


def run_app(queue):
    print("=" * 44)
    print("🎤 Karaoke Queue")
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
