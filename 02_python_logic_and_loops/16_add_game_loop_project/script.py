# Challenge: Add a Game Loop
# Right now the game ends after a single word. Add the ability to play multiple rounds and quit out of the game at any point.

# 1. Wrap the game code in a loop that runs for 5 rounds. 
# 2. Display the round number at the beginning of each round. 
# 3. Give the player a way to quit early by typing 'quit'.
#    * Hint: you'll want to break out of the loop when they do.

import random

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

