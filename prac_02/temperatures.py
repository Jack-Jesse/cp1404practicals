"""
Temperatures
CP1404/CP5632 - Practical
A program to convert celsius to fahrenheit or fahrenheit to celsius.
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """Convert celsius to fahrenheit or fahrenheit to celsius."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_celsius()
            fahrenheit = convert_fahrenheit_to_celsius(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = get_fahrenheit()
            celsius = convert_celsius_to_fahrenheit(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(fahrenheit):
    """Convert celsius to fahrenheit."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def get_fahrenheit():
    """Get fahrenheit."""
    fahrenheit = float(input("Fahrenheit: "))
    return fahrenheit


def convert_fahrenheit_to_celsius(celsius):
    """Convert fahrenheit to celsius."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_celsius():
    """Get celsius."""
    celsius = float(input("Celsius: "))
    return celsius


main()
