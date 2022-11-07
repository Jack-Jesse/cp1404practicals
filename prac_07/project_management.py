"""
Project
Estimate: 120 minutes
Actual:
"""

import datetime
from project import Project
from operator import attrgetter

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
            load_file(filename, projects)
        elif choice == "S":
            save_file()
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date()
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def load_file(filename, projects):
    with open(filename, "r", encoding="utf-8") as in_file:
        in_file.readline()  # remove the first line
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)


def save_file():
    print("Save file")


def display_projects(projects):
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        completed_projects.append(project) if project.is_complete() else incomplete_projects.append(project)
    incomplete_projects.sort(key=attrgetter("priority"))
    completed_projects.sort(key=attrgetter("priority"))
    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        print(f"\t{incomplete_project}")
    print("Completed projects:")
    for completed_project in completed_projects:
        print(f"\t{completed_project}")


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = int(input("Project choice: "))
    project = projects[choice]
    print(projects[choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = int(input("New Priority: "))
    project.completion_percentage = new_percentage
    project.priority = new_priority


def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date: ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


def filter_projects_by_date():
    print("Filter projects by date")


main()
