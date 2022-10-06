"""
Quick picks
CP1404/CP5632 Practical
A program that prints random numbers in multiple rows decided by the user.
"""

import random
MINIMUM = 1
MAXIMUM = 45
NUMBER_OF_RANDOM_NUMBERS = 6

number_of_rows = int(input("How many quick picks: "))
for row in range(number_of_rows):
    for i in range(NUMBER_OF_RANDOM_NUMBERS):
        print(f"{random.randint(MINIMUM, MAXIMUM):> 3}", end="")
    print("")
