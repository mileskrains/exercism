# Connect

Compute the result for a game of Hex / Polygon.

The abstract boardgame known as
[Hex](https://en.wikipedia.org/wiki/Hex_%28board_game%29) / Polygon /
CON-TAC-TIX is quite simple in rules, though complex in practice. Two players
place stones on a rhombus with hexagonal fields. The player to connect his/her
stones to the opposite side first wins. The four sides of the rhombus are
divided between the two players (i.e. one player gets assigned a side and the
side directly opposite it and the other player gets assigned the two other
sides).

Your goal is to build a program that given a simple representation of a board
computes the winner (or lack thereof). Note that all games need not be "fair".
(For example, players may have mismatched piece counts.)

The boards look like this (with spaces added for readability, which won't be in
the representation passed to your code):

```text
. O . X .
 . X X O .
  O O O X .
   . X O X O
    X O O O X
```

"Player `O`" plays from top to bottom, "Player `X`" plays from left to right. In
the above example `O` has made a connection from left to right but nobody has
won since `O` didn't connect top and bottom.

## Exception messages

Sometimes it is necessary to raise an exception. When you do this, you should include a meaningful error message to
indicate what the source of the error is. This makes your code more readable and helps significantly with debugging. Not
every exercise will require you to raise an exception, but for those that do, the tests will only pass if you include
a message.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of
`raise Exception`, you shold write:

```python
raise Exception("Meaningful message indicating the source of the error")
```


## Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `exercism/python/<exerciseName>` directory.

For example, if you're submitting `bob.py` for the Bob exercise, the submit command would be something like `exercism submit <path_to_exercism_dir>/python/bob/bob.py`.

For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).


## Submitting Incomplete Solutions
It's possible to submit an incomplete solution so you can see how others have completed the exercise.
