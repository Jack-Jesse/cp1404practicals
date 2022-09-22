"""
menus
CP1404/CP5632 - Practical
A program to get name and print message
"""

MENU = "(H)Hello\n(G)Goodbye\n(Q)Quit"

name = input("Name: ")
print(MENU)
choice = input("Choice: ").lower()
while choice != "q":
    if choice == "h":
        print(f"Hello {name}")
    elif choice == "g":
        print(f"Goodbye {name}")
    else:
        print("Invalid entry")
    print(MENU)
    choice = input("Choice: ").lower()
print("Thanks for using menus!")
