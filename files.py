# This is where you will complete prompts 1-10
# PROMPT 1: Write the relative-path string needed to open supplies.txt from files.py
""" data/supplies.txt  """

# PROMPT 2: Write a function named print_line_lengths(filename). Requirements:
# •	Open the file at  filename .
# •	Print the length of every original line, including its newline character if present.
# •	Close the file.

def print_line_lengths(filename):
    with open(filename) as file: # opens the file stored in the "filename" string variable, makes it accessible
        for line in file: # parses every line in "file" with the "line" variable
            print(len(line)) # prints the number of characters in the current line
    print("\n")

# PROMPT 3: Write a function named  print_clean_supplies(filename) .
# Requirements:
# •	Use  with open(...) .
# •	Print each line after removing leading/trailing whitespace.
# •	Do not remove blank lines; print them as blank lines.

def print_clean_supplies(filename):
    with open(filename) as file:
        for line in file:
            print(line.strip())
    print("\n")

# PROMPT 4: Write a function named  count_supply(filename, target) .
# Requirements:
# •	Return how many lines match  target .
# •	Ignore capitalization and surrounding whitespace.
# •	Do not prompt the user; use the  target  parameter.

def count_supply(filename, target):
    line_count = 0
    lower_target = target.lower()
    with open(filename) as file:
        for line in file:
            lowercase = line.strip().lower()
            if lowercase == lower_target:
                line_count += 1
    return line_count

def main():
    # prompt 2
    print_line_lengths("data/supplies.txt") # calls "supplies" text file for manual testing

    # prompt 3
    print_clean_supplies("data/supplies.txt")

    # prompt 4
    print(count_supply("data/supplies.txt", "pencils")) # 2
    print(count_supply("data/supplies.txt", "markers")) # 1
    print(count_supply("data/supplies.txt", "paper")) # 0


if __name__ == "__main__": # run-guard, prevents main from accidentally running when using pytest
    main()