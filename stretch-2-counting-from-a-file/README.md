# Stretch 2: Counting, from a file

Files: `counting_from_a_file.py`, `rainfall.txt`

Optional. Yesterday's dictionary, today's data source. The counting pattern you
met on Day 6, running on lines that came out of a file.

## Predict

Three bands: Very wet at 120 or above, Wet at 80 or above, Dry below that. How
many stations land in each?

What does the dictionary look like when it is printed?

## Run

Execute and compare.

## Investigate

- `bands[band] = bands.get(band, 0) + 1` is the line from Day 6, unchanged. The
  only thing that has changed is where the data came from. Why did none of the
  dictionary code need altering?
- The bands appear in the printed dictionary in a particular order. What decides
  it? It is not alphabetical and it is not the order in the `if`.
- A station reporting exactly 80 lands in one band rather than another. Which,
  and which character decides it?

## Modify

- Add a fourth band and predict the counts before running.
- Report the bands in a sensible order rather than the order they happened to
  appear.
