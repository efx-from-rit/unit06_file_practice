# Unit 6: Files and Exception Handling

This repository contains Python practice programs for Unit 6. The goal of this unit is to learn how to read and process data from text and CSV files, handle common runtime errors, and break larger problems into smaller helper functions.

## Topics Practiced

- Opening files with relative paths
- Reading text files one line at a time
- Cleaning text with `.strip()` and `.lower()`
- Searching through files
- Splitting strings with `.split()`
- Processing simple CSV files
- Skipping CSV header rows with `next()`
- Using `with open(...)` to automatically close files
- Handling `FileNotFoundError` and `ValueError`
- Using the Python `csv` module for CSV fields that contain commas
- Creating helper functions for a book-cipher program

## Project Structure

```text
.
├── files.py
├── activities.py
├── csvfun.py
├── bookcipher.py
├── README.md
└── data/
    ├── supplies.txt
    ├── scores.csv
    ├── locations.csv
    ├── mixed_numbers.txt
    └── scores_bad.csv