"""
shop calculator
CP1404/CP5632 - Practical
A program that calculates the total of each item entered
"""

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
else:
    for item in range(number_of_items):
        price_of_item = float(input("Item price: "))
        total += price_of_item
    if total > 100:
        total -= total * 0.1
    else:
        total = total
    print(f"Total price for {number_of_items} items is {total:.2f}")