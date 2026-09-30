# Stretch 1: When the file is not there

File: `missing_file.py`

Optional, and worth doing if you finish early. Every program that reads a file
can be run in a situation where that file does not exist.

## Predict

`notes.txt` does not exist in this folder. What does the program print?

## Run

Execute it. Then create `notes.txt` next to the program, put a line in it, and
run it again.

## Investigate

- Read the error message the first block caught. What does it tell you, and what
  does it not tell you?
- The second block ends up with an empty list rather than stopping. Is that
  always the right thing to do? When would you rather the program stopped?
- Rename `rainfall.txt` in one of the other activities and run that activity.
  Compare the error you get with the one here.

## Modify

- Make the program tell the user which file it could not find, in plain English,
  without showing them a traceback.
- Make it create the file if it is missing, then read it.
