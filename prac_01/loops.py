"""
Loops
CP1404/CP5632 - Practical
A program that has various loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 110, 10):
    print(i, end=" ")
print()

# b.
for i in range(20, 0, -1):
    print(i, end=" ")
print()

# c.
number = int(input("Enter number: "))
for i in range(number):
    print("*", end="")

# d.
number = int(input("Enter number: "))
for i in range(number + 1):
    print('*' * i)
