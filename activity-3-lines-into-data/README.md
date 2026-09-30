# Activity 3: Turning lines into data

Files: `rainfall_summary.py`, `rainfall.txt`

A working program. It reads the five stations, works out the total, the average
and which stations were wet, and prints a summary. Nothing is written back out.

## Predict

- What is the total rainfall?
- What is the average, to one decimal place?
- Which stations are at or above the 100 mm threshold?

Work all three out by hand from `rainfall.txt` before you run anything.

## Run

Execute it and compare.

## Investigate

- `line.strip().split(",")` does two jobs in one line. Say what each one does,
  and predict what would happen if the `.strip()` were removed. Then remove it
  and find out.
- `int(millimetres_text)` converts text into a number. Why is that necessary at
  all? What is `"82" + "141"` compared with `82 + 141`?
- `total` and `count` both start at 0 before the loop, for the same reason the
  empty list did on Day 5. Say what that reason is.
- Which comparison decides whether a station counts as wet, and what happens to
  a station that reports exactly 100?

## Modify

- Report the driest station as well as the wettest.
- Report how many stations were below the threshold, without counting by hand.
- Change the threshold to 90 and predict which stations move before you run it.

> This program does exactly what this week's assignment task does: read lines,
> split each one, convert the number, keep a running total, decide something
> about each record. The only thing missing is writing the answer to a file.
