"""
Wimbledon
CP1404/CP5632 Practical
Estimate: 60 minutes
"""


def main():
    champion_to_count = {}
    data = load_file("wimbledon.csv")
    champions = [champion[:][2] for champion in data]
    for champion in champions:
        try:
            champion_to_count[champion] += 1
        except KeyError:
            champion_to_count[champion] = 1
    for champion, number_of_wins in champion_to_count.items():
        print(champion, number_of_wins)
    winning_countries = sorted({country[:][1] for country in data})
    print(", ".join(winning_countries))


def load_file(filename):
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        first_line = in_file.readline()
        data = [line.split(",") for line in in_file]
    return data


main()
