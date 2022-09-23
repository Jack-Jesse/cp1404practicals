"""
Score Menu
CP1404/CP5632 - Practical
A program that has a menu of things to do with a score.
"""

MENU = "(R)esult\n(S)tars\n(Q)uit"


def main():
    """Get valid score, then give menu options."""
    score = get_valid_score()
    print(MENU)
    choice = input("Choice >>> ").upper()
    while choice != "Q":
        if choice == "R":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid input error")
        print(MENU)
        choice = input("Choice >>> ").upper()
    print("Thanks for using")


def get_valid_score():
    """Get valid score."""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determine result."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(length_of_stars):
    """Print stars a certain length."""
    print("*" * length_of_stars)


main()
