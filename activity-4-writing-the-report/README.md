# Activity 4: Writing the report

Files: `rainfall_report.py`, `rainfall.txt`

The same data as activity 3, but the summary now goes into a file rather than
onto the screen. A working program.

## Predict

`report.txt` does not exist yet. Write out, line by line, exactly what you think
it will contain after one run. Include the average line.

Then predict what the program prints to the screen.

## Run

Execute it, then open `report.txt` and compare against what you wrote.

## Investigate

- The report file is opened once, before the loop, and the loop writes into it.
  What would happen if the `open` were inside the loop instead? Predict first,
  then try it, then put it back.
- The average line is written after the loop finishes, not inside it. Why does
  that matter? Move it inside and look at what you get.
- `with open(...)` closes the file for you when the block ends. What is the
  evidence that it has closed, given nothing in the code says `close`?
- `report.write(...)` needs a `\n` on the end of every line. Take one out and
  see what the file looks like.

## Modify

- Add a line at the top of the report saying how many stations there were.
- Report the total as well as the average.
- Write only the wet stations to the report, and print the dry ones to the
  screen instead.

> The three Investigate questions above are, between them, the whole of this
> week's assignment task. If you can answer them without running anything, the
> task will take you half the time.
