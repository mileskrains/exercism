# Markdown

Refactor a Markdown parser.

The markdown exercise is a refactoring exercise. There is code that parses a
given string with [Markdown
syntax](https://guides.github.com/features/mastering-markdown/) and returns the
associated HTML for that string. Even though this code is confusingly written
and hard to follow, somehow it works and all the tests are passing! Your
challenge is to re-write this code to make it easier to read and maintain
while still making sure that all the tests keep passing.

It would be helpful if you made notes of what you did in your refactoring in
comments so reviewers can see that, but it isn't strictly necessary. The most
important thing is to make the code better!

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
