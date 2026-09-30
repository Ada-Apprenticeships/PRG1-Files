"""
Rainfall Summary

Reads a month's rainfall from five weather stations and prints a
summary. Reading only: nothing is written back out.

Each line of rainfall.txt is a station name and a number of
millimetres, separated by a comma.
"""

WET_THRESHOLD = 100

with open("rainfall.txt", "r") as f:
    lines = f.readlines()

total = 0
count = 0
wet_stations = []

for line in lines:
    station, millimetres_text = line.strip().split(",")
    millimetres = int(millimetres_text)

    total = total + millimetres
    count = count + 1

    if millimetres >= WET_THRESHOLD:
        wet_stations.append(station)

print(f"{count} stations reported")
print(f"Total rainfall: {total} mm")
print(f"Average: {total / count:.1f} mm")
print(f"At or above {WET_THRESHOLD} mm: {wet_stations}")
