# Activity 2: The username checker

Files: `username_check.py`, `test_usernames.txt`

A working program. It reads a file of usernames, decides whether each one is
valid, and writes the result to a log. Some of the usernames have spaces around
them, which is what makes it interesting.

Open `test_usernames.txt` first. Fourteen lines, and some of them are not what
they look like.

## Predict

For each of these, will the program say `True` or `False`?

| Username in the file | Your prediction |
|---|---|
| `zara` | |
| ` bob ` (spaces either side) | |
| `   ` (spaces only) | |
| The empty line at the end | |

Then: how many lines will the log file have after one run?

## Run

Execute it. Compare against your predictions, then open
`username_validation_log.txt` and count the lines.

## Investigate

- `.strip()` removes whitespace from both ends of a string. Which of the
  usernames does it change, and which does it leave alone?
- `is_valid_username` strips before checking the length. What happens to the
  spaces-only line if you take the `.strip()` out? Predict, then try it.
- The log has one more line than there are usernames in the file. Work out where
  the extra one comes from. `username_data.split("\n")` is the line to look at.
- Run the program a second time. Does the log get replaced or added to? Find the
  single character in the code that decides that.

## Modify

- Remove the `.strip()` from line 12 and run it again. Which usernames change
  from Valid to Invalid, or the other way round?
- Make a username of fewer than three characters invalid. Should you check the
  length before or after stripping? Try both and see.
- Make the log replace itself on each run rather than growing.

> The last Modify is the one to remember. One character decides whether a
> program adds to a file or wipes it, and both look equally reasonable when you
> are reading the code.
