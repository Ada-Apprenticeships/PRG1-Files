# PRG1: Files (PRIM activities)

Day 7. Six activities plus two stretch folders, each in its own folder, each
with the code and its tasks together in one place.

## PRIM

| Step | What you do |
|---|---|
| **Predict** | Say what the code will do **before** you run it. Write it down. |
| **Run** | Run it. Compare against your prediction. |
| **Investigate** | Work out *why* it behaves that way. |
| **Modify** | Change something specific, predicting the effect before each change. |

With files there is a second thing to predict: not just what appears on the
screen, but what ends up in the file. Predict both, every time.

## The activities

### Morning: reading from files

| Folder | Focus |
|---|---|
| `activity-1-reading-a-file/` | Three ways to read the same file, and what comes back |
| `activity-2-username-checker/` | A working validator: stray whitespace, and a log that grows |
| `activity-3-lines-into-data/` | Splitting a line into fields and turning text into numbers |

### Afternoon: writing reports

| Folder | Focus |
|---|---|
| `activity-4-writing-the-report/` | The same summary, written to a file instead of the screen |
| `activity-5-w-versus-a/` | Ten minutes. The difference between replacing a file and adding to it |
| `activity-6-broken-report/` | Three faults in a report that looks entirely reasonable |

### Stretch

| Folder | Focus |
|---|---|
| `stretch-1-when-the-file-is-missing/` | What happens when the file is not there |
| `stretch-2-counting-from-a-file/` | Day 6's counting pattern on data read from a file |

## The same data, all day

Activities 1, 3, 4 and 6 all use `rainfall.txt`: five weather stations and a
month's rainfall in millimetres. It is deliberately the same file throughout, so
that the only thing changing from activity to activity is what the code does
with it.

Activity 6's copy is slightly untidy. That is part of the activity.

## How to work through these

Work in pairs. One drives, the other reads and questions, then swap at each new
activity.

You are **not** expected to finish everything. Activity 3 in the morning and
activity 5 in the afternoon are the two that matter most. Two done properly
beats six rushed.

## Running a file

Each activity's data file sits in that activity's own folder, so change into the
folder first:

```
cd activity-1-reading-a-file
python reading_a_file.py
```

If `python` is not recognised, use `python3` instead.

## Reference

`reference/` holds supporting material. Do not open anything in there until
after the class discussion it belongs to.
