"""
My guitars
CP1404/CP5632 Practical
Estimate: 30 minutes 6:00
Actual:
"""
FILENAME = "guitars.csv"


def main():
    """Sort the guitars into a sorted list."""
    guitars = []
    load_file(FILENAME, guitars)
    guitars.sort()


def load_file(filename, guitars):
    """Load file into a list."""
    with open(filename, "r") as in_file:
        for line in in_file:
            guitars.append(line.strip().split(","))


main()
