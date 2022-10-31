"""
Guitar test
CP1404/CP5632 Practical
A program for testing Guitar class
"""

from guitar import Guitar

my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another guitar", 2013, 800.00)
print(my_guitar.get_age())
print(another_guitar.get_age())
print(my_guitar.is_vintage())
print(another_guitar.is_vintage())
