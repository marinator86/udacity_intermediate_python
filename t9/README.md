## T9

In this final exercise, you'll combine what you've learned about data types to build a predictive text algorithm.

This exercise comes in three

You'll write three functions:

```
def parse_content(content):
    pass

def make_tree(words):
    pass

def predict(tree, numbers):
    pass
```

The `parse_content` function should accept the text contents of a file and return a dictionary mapping a word to its frequency.

The `make_tree` function should return a dictionary mapping letters recursively in a tree structure – using the sentinel `$` for the end-of-word character. For example, the words (`band` ,`ban`, `bar`, `can`) should become the tree:

```
.
|- b
|  |- a
|     |- r
|     |  |_ $
|     |_ n
|        |- $
|        |_ d
|           |_ $
|_ c
    |_ a
        |_ n
            |_ $
```

The `predict` function should take in an iterable of numbers, and return a sorted collection of the most common words that start with a prefix of any number of the letters associated with those numbers.

For more information on T9, see <a href="https://en.wikipedia.org/wiki/T9_(predictive_text)" target="_blank">Wikipedia</a>.