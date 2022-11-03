"""
Project

"""

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project 
- (U)pdate project 
- (Q)uit"""


def main():
    load_file()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            load_file()
        elif choice == "S":
            save_file()
        elif choice == "D":
            display_projects()
        elif choice == "F":
            filter_projects_by_date()
        elif choice == "A":
            add_new_project()
        elif choice == "U":
            update_project()
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def update_project():
    print("Update project")


def add_new_project():
    print("add new project")


def filter_projects_by_date():
    print("Filter projects by date")


def display_projects():
    print("Display projects")


def load_file():
    print("Load file")


def save_file():
    print("Save file")


main()
