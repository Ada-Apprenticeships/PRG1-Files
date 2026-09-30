# Activity 6: The report that lies

Files: `broken_report.py`, `rainfall.txt`

The same rainfall report, with three faults. Nothing crashes. The report looks
like a report.

Note: this activity's `rainfall.txt` came from a different source and is not
quite as tidy as the one you have been using. That is deliberate, and it is
relevant.

## Predict

You already know what the correct report looks like from activity 4. Write it
out again, including the average.

Also predict: what happens if you run this program twice?

## Run

Execute it once and compare the report against what you wrote. Then execute it
again and look at the file a second time.

## Investigate

- The screen says six stations. The report has five lines. Both numbers come
  from the same file. Work out which one is right, and where the sixth came
  from. `contents.split("\n")` is the line to look at.
- The average is 79.8, and you know it should not be. Which number in the
  division is wrong, and why is it wrong by exactly one?
- Cardiff is on the watch list and is not labelled as watched. Look at the
  station name in the report, character by character. Then look at
  `rainfall.txt` in a text editor.
- Running the program twice does not give you the same report twice. One
  character is responsible.

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. Then delete `report.txt`, run the program twice, and check that
you get the same five stations and the same average both times.

## Stretch

Optional. Make the program cope with a `rainfall.txt` where any station name
might have stray spaces around it, rather than just the one that does.

> None of these three is a typo you could see by looking. Each one needed you to
> know what the right answer was before you started. That is why activity 4 came
> first.
