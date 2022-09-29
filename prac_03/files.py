"""
Files
CP1404/CP5632 - Practical

"""

# 1.
name = input("Name: ")
out_file = open(f"{name}.txt", "w")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("Jack.txt", "r")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

# 3.
total = 0
in_file = open("numbers.txt", "r")
for line in range(0, 2):
    number = int(in_file.read(3))
    total += number
in_file.close()
print(total)

# 4.
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
