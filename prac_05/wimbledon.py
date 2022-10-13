"""
Wimbledon
CP1404/CP5632 Practical
Estimate: 60 minutes
Actual: 80 minutes
A program to load data from csv and print it neatly.
"""


def main():
    """Sort data from csv and display data neatly."""
    champion_to_count = {}
    data = load_file("wimbledon.csv")
    champions = [champion[:][2] for champion in data]
    count_champion_wins(champion_to_count, champions)
    print_champion_number_of_wins(champion_to_count)
    winning_countries = sorted({country[:][1] for country in data})
    print(", ".join(winning_countries))


def print_champion_number_of_wins(champion_to_count):
    """Print the champions with their number of wins."""
    for champion, number_of_wins in champion_to_count.items():
        print(champion, number_of_wins)


def count_champion_wins(champion_to_count, champions):
    """Count the number of wins for each champion."""
    for champion in champions:
        try:
            champion_to_count[champion] += 1
        except KeyError:
            champion_to_count[champion] = 1


def load_file(filename):
    """Load file data."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        data = [line.split(",") for line in in_file]
    return data


main()
