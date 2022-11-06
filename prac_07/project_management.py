"""
Project
Estimate: 120 minutes
Actual:
"""

import datetime
from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""

FILENAME = "project.txt"


def main():
    projects = []
    load_file(FILENAME, projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            load_file(FILENAME, projects)
        elif choice == "S":
            save_file()
        elif choice == "D":
            display_projects(projects)
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


def load_file(filename, projects):
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # remove the first line
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], parts[2], float(parts[3]), parts[4])
            projects.append(project)


def save_file():
    print("Save file")


def display_projects(projects):
    for project in projects:
        print(project)


def update_project():
    print("Update project")


def add_new_project():
    print("add new project")


def filter_projects_by_date():
    print("Filter projects by date")


main()
