"""
Optional stretch. Yesterday's dictionary, today's file.

Counts how many stations fall into each band, using the counting
pattern from Day 6 on data that came out of a file.
"""

with open("rainfall.txt", "r") as f:
    lines = f.readlines()

bands = {}

for line in lines:
    station, millimetres_text = line.strip().split(",")
    millimetres = int(millimetres_text)

    if millimetres >= 120:
        band = "Very wet"
    elif millimetres >= 80:
        band = "Wet"
    else:
        band = "Dry"

    bands[band] = bands.get(band, 0) + 1

print(bands)
for band, number in bands.items():
    print(f"{band}: {number}")
