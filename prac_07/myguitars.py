"""
My guitars
CP1404/CP5632 Practical
Estimate: 30 minutes
Actual: 60 minutes
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Sort the guitars into a sorted list."""
    guitars = []
    load_file(FILENAME, guitars)
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitars.append(Guitar(name, year, cost))
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    save_file(FILENAME, guitars)


def load_file(filename, guitars):
    """Load file into a list."""
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


def save_file(filename, guitars):
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
