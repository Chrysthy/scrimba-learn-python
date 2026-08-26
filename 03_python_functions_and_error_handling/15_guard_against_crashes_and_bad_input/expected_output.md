# Condition: the queue is empty:
```
The queue is currently empty.

Options: add / next / top / remove / quit
```

# Condition: attempt to move a singer to the top of the queue when there are fewer than two singers:
```
> top

You need at least two singers in the queue to move someone to the top.
```

# Condition: Trying to move a singer to the top of the queue with a position that doesn't exist:
```
> top

Who do you want to move to the top? Enter a number: 5

There's no singer at position 5.

# Condition: enter a blank name or song:

```
> add

Name:
Song:

Oops! I need a name and a song to add someone to the queue.
```

# Condition: remove singer on an empty queue.
> remove

Oops! There's no one left to remove!

The queue is currently empty.

Options: add / next / top / remove / quit
```