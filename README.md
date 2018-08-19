# Storymode

A text adventure generator for the command line

## Usage

```bash
$ python storymode.py <story_file>
```

## Story files

Story files are text files with three different kinds of lines:

* An entry: defines a prompt with choices to choose from. It is composed of a key, identifying the entry and a prompt, like `<key>::<prompt>`.
* A choice: defines a choice to be presented with an entry. It comes after an entry and is composed of text and a reference to an entry key, like `<text>::<reference>`
* A comment: Just that a comment that is not parsed and serves for documentation

An example can be found at `tests/data/test.txt`

### Structure

There are two mandatory entries designated with the keys, `start` and `end`. You might imagine what the role these entries play.

### Caveats

* `::` are reserved for story structuring.
* Entries (and there choices) must be seperated by other by at least one new line
