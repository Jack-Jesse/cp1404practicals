"""
Emails
CP1404/CP5632 Practical
Estimate: 30 minutes
Actual: 45 minutes
A program that takes name from users email and add to dictionary.
"""

name_to_email = {}
email = input("email: ")
while email != "":
    names = email[:email.index("@")].split(".")  # Creating a list of first and last names.
    full_name = " ".join(names).title()  # Taking the names from list and joining them to create full name.
    print(f"Is your name {full_name}")
    confirm_name = input("Y/n: ").lower()
    if confirm_name == "n":
        full_name = input("name: ")
    name_to_email[full_name] = email  # Add the key and value to dictionary.
    email = input("Email: ")
for full_name, email in name_to_email.items():  # Accessing the keys and their values.
    print(f"{full_name} ({email})")
