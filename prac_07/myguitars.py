"""
My guitars
CP1404/CP5632 Practical
Estimate: 30 minutes 6:00
Actual: 44 minutes
"""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Sort the guitars into a sorted list."""
    guitars = []
    load_file(FILENAME, guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def load_file(filename, guitars):
    """Load file into a list."""
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


main()
