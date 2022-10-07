"""
Subject reader
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_details = []
    input_file = open(FILENAME)
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        data_points = line.split(",")
        data_points[-1] = int(data_points[-1])
        subject_details.append(data_points)
    input_file.close()
    return subject_details


def print_subject_details(data):
    for i in range(len(data)):
        print(f"{data[i][-1]} is taught by {data[i][-1]} and has {data[i][-1]} students")


main()
