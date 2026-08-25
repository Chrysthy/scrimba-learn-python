# Sing Line

Sing Line is a Python command-line application for managing a karaoke queue.

Users can add singers, call the next performer, move someone to the top of the queue, and remove singers.

<br>

## Demo

![Sing Line Demo](./assets/sing-line-demo.gif)

<br>

## How It Works

The application keeps track of singers and their selected songs in a queue.

Users can manage the queue using simple commands:

- `add` to add a new singer and song
- `next` to call the next singer
- `top` to move someone to the top of the queue
- `remove` to remove a singer
- `quit` to close the application

The current queue is displayed after each action, showing the position, singer name, and selected song.

<br>

## Example

```text
============================================
🎤 Welcome to Sing Line 🎤
============================================

Current queue:

1. Annie - Dancing Queen
2. Allen - Country Roads

Options: add / next / top / remove / quit

> add

Name: Sarah
Song: Flowers

Added Sarah to the queue

Current queue:

1. Annie - Dancing Queen
2. Allen - Country Roads
3. Sarah - Flowers

Options: add / next / top / remove / quit

> next

NOW UP: Annie - Dancing Queen
````
<br>

## Concepts Practiced

* Variables
* Lists
* Tuples
* Functions
* While loops
* For loops
* Conditional statements
* User input
* String methods
* List manipulation
* `enumerate()`
* `append()`
* `pop()`
* `insert()`
* `remove()`
* Tuple unpacking
* F-strings

<br>

## How to Run


1. Clone the repository:

```bash
git clone https://github.com/Chrysthy/scrimba-learn-python.git
```

2. Open the project directory:

```bash
cd scrimba-learn-python/projects/03_sing_line
```

3. Run the Python file:

```bash
python main.py
```
<br>

## Possible Improvements

* Add input validation
* Handle an empty queue safely
* Prevent invalid queue positions
* Allow users to edit a singer or song
* Save and load the queue from a file
* Add estimated waiting time
* Improve handling of duplicate names
* Add a graphical interface

<br>

## Course

This project was developed as part of the Learn Python course by Scrimba.

---
<br>

[← Back to the main README](../../README.md)


