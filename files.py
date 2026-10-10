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

def print_clean_supplies(filename):
    with open(filename) as file:
        for line in file:
            print(line.strip())

def main():
    print_line_lengths("data/supplies.txt") # calls "supplies" text file for manual testing
    print_clean_supplies("data/supplies.txt")

if __name__ == "__main__": # run-guard, prevents main from accidentally running when using pytest
    main()