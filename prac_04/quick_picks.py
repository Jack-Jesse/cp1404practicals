"""
Quick picks
CP1404/CP5632 Practical
A program that prints random numbers in multiple rows decided by the user.
"""

import random
MINIMUM = 1
MAXIMUM = 45
NUMBERS_PER_LINE = 6

number_of_rows = int(input("How many quick picks: "))
for row in range(number_of_rows):
    random_numbers = []
    for i in range(NUMBERS_PER_LINE):
        random_numbers.append(random.randint(MINIMUM, MAXIMUM))
    quick_picks = sorted(random_numbers)
    for pick in quick_picks:
        print(f"{pick:>2}", end=" ")
    print()
