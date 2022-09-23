"""
Password stars
CP1404/CP5632 - Practical
A program to print a star for every character in password.
"""

MINIMUM_PASSWORD_LENGTH = 8


def main():
    """Let user know if password is too short, then print password when valid."""
    password = get_password()
    print_stars_length_of(password)


def print_stars_length_of(password):
    """Print stars the length string."""
    print("*" * len(password))


def get_password():
    """Keep prompting for password untill valid length."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password is too short.")
        password = input("Enter password: ")
    return password


main()
