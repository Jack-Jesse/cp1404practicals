"""
sequence
CP1404/CP5632 - Practical
A program to print a specific type of number from x to y
"""

MENU = "(E)ven numbers\n(O)dd numbers\n(S)quare numbers\n(Q)uit"

start_number = int(input("Enter number to start from: "))
end_number = int(input("Enter number to end at: "))
print(MENU)
choice = input("Choice: ").lower()
while choice != "q":
    if choice == "e":
        for i in range(start_number, end_number):
            if i % 2 == 0:
                print(i)
    elif choice == "o":
        for i in range(start_number, end_number):
            if i % 2 == 1:
                print(i)
    elif choice == "s":
        for i in range(start_number, end_number):
            print(i * i)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Choice: ").lower()
print("Thanks for using sequence program")





