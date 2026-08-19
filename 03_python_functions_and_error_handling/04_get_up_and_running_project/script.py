# - show a list of commands 
# - show the queue 
# - respond to commands: 
#   - add a singer
#   - remove a singer
#   - quit or exit the program (keep running until user quits)


def show_queue(queue):
    """Print everyone currently in the queue"""
    print("[the queue goes here]")

queue = [("Annie", "Dancing Queen"), ("Allen", "Country Roads")]

def run_app(queue):
    print("=" * 44)
    print("Welcome to Sing Out: A Karaoke Queue Manager")
    print("=" * 44)

    is_running = True

    while is_running:

        print("Options:  add / remove / quit")

        command = input("> ")

        if command == "quit":
            is_running = False
            print("Good Night!")

