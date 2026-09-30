# Activity 5: w versus a

File: `two_modes.py`

Ten minutes, and the most important ten minutes of the day.

## Predict

The program writes one line to each of two files. It then reports how many lines
each file has.

- What does it report the first time you run it?
- What does it report the second time?
- What about the fifth time?

## Run

Run it. Then run it again. Then run it a third time. Watch the two numbers.

## Investigate

- One file stays at one line forever. The other grows. The only difference
  between them is a single character. Find it.
- `"w"` and `"a"` are both perfectly valid. Describe, in one sentence each, the
  job each one is right for.
- Delete both files and run it once more. Does `"a"` complain that the file was
  not there?
- What would happen if a program opened a file with `"w"` every time round a
  loop of five records? Work it out before you try it.

## Modify

- Swap the two modes over and predict the result before running.
- Make the appending file start fresh once, then keep appending afterwards.

> That last Investigate question is a real fault that appears in real code, and
> it is very hard to spot by reading, because a file opened with `"w"` inside a
> loop looks exactly like a file opened with `"w"` outside one.
