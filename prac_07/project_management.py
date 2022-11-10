"""
Project
Estimate: 120 minutes
Actual: 6 hours
"""

import datetime
from operator import attrgetter
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
    """Run menu program for project management with various options."""
    projects = []
    load_file(FILENAME, projects)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename: ")
            load_file(filename, projects)
        elif choice == "S":
            save_file(projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()


def load_file(filename, projects):
    """Load file from file in to projects list."""
    del projects[:]  # Delete previously loaded projects to avoid duplicates
    try:
        with open(filename, "r", encoding="utf-8") as in_file:
            in_file.readline()  # remove the first line of headings
            for line in in_file:
                parts = line.strip().split("\t")
                project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
                projects.append(project)
    except FileNotFoundError:
        print("File not found")


def save_file(projects):
    """Save projects to file selected by user through input."""
    filename = input("Filename: ")
    with open(filename, "w", encoding="utf-8") as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t "
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects neatly formatted."""
    incomplete_projects = []
    completed_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(project)
        else:
            incomplete_projects.append(project)
    incomplete_projects.sort(key=attrgetter("priority"))
    completed_projects.sort(key=attrgetter("priority"))
    print("Incomplete projects:")
    for incomplete_project in incomplete_projects:
        print(f"\t{incomplete_project}")
    print("Completed projects:")
    for completed_project in completed_projects:
        print(f"\t{completed_project}")


def update_project(projects):
    """Update projects with new percentage and new priority entered by the user."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    choice = get_valid_project(projects)
    project = projects[choice]
    print(project)
    new_percentage = get_valid_number("New Percentage: ")
    new_priority = get_valid_number("New Priority: ")
    project.completion_percentage = new_percentage
    project.priority = new_priority


def get_valid_number(sentence):
    """Get valid number with error checking."""
    is_valid_number = False
    while not is_valid_number:
        try:
            number = int(input(sentence))
            if number < 0:
                print("Number must be >= 0")
            elif number > 100:
                print("Number can only be <= 100")
            else:
                is_valid_number = True
        except ValueError:
            print("Must enter a number")
    return number


def get_valid_project(projects):
    """Get valid project with error checking."""
    is_valid_input = False
    while not is_valid_input:
        try:
            choice = int(input("Project choice: "))
            if choice < 0:
                print("Number must be >= 0")
            elif choice > len(projects) - 1:
                print(f"Number must be <= {len(projects) - 1}")
            else:
                is_valid_input = True
        except ValueError:
            print("Must enter a number")
    return choice


def add_new_project(projects):
    """Add new project to the projects list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date: ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    percent_complete = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost_estimate, percent_complete)
    projects.append(project)


def filter_projects_by_date(projects):
    """Display projects filtered by date."""
    filtered_projects = []
    is_valid_date = False
    while not is_valid_date:
        try:
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Enter valid date format (dd/mm/yy)")
    for project in projects:
        if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date() >= date:
            filtered_projects.append(project)
    filtered_projects.sort(key=attrgetter("start_date"), reverse=True)
    for filtered_project in filtered_projects:
        print(filtered_project)


main()
