# Activity 1: Reading a file

Files: `reading_a_file.py`, `rainfall.txt`

The same file, read three different ways. Open `rainfall.txt` and look at it
first. Five lines, each a station name and a number of millimetres.

## Predict

- What does the first block print?
- What does the second block print? It prints the list itself, not the lines
  one by one, so write out what you think that list looks like.
- How many lines does it say there are?
- What does the third block print, and why are the square brackets there?

## Run

Execute it and compare. The second and third blocks are where predictions
usually go wrong.

## Investigate

- Look hard at the list the second block printed. There is something on the end
  of every item that is not a station name or a number. What is it, and where
  did it come from?
- The third block wraps each line in square brackets. What do those brackets
  reveal that the first block hid?
- The first block printed a blank line at the end. Why?
- `.read()`, `.readlines()` and looping over the file all read the same file.
  When would you want each one?

## Modify

- Print only the third line of the file.
- Print the file with the line endings removed, so there are no gaps.
- Add a sixth station to `rainfall.txt` and predict what changes before you run
  it again.

> Every line you read from a file arrives with a newline character on the end.
> Forgetting that is the single most common file-handling fault, and you will
> meet it again in about twenty minutes.
