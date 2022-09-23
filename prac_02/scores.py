"""
broken scores
CP1404/CP5632 - Practical
A program to determine the result of a score.
"""
import random


def main():
    score = get_score()
    result = determine_score(score)
    random_score = random.randint(0, 100)
    random_score_result = determine_score(random_score)
    print(result)
    print(random_score, random_score_result)


def get_score():
    score = float(input("Enter score: "))
    return score


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
