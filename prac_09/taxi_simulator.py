"""
Taxi Simulator
estimate: 60 minutes
actual:
"""
from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(f"Bill to date: ${bill_to_date:,.2f}")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            display_taxis(taxis)
            current_taxi = get_valid_taxi_choice(taxis)
        elif choice == "d":
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            drive_distance = int(input("Drive how far? "))
            current_taxi.start_fare()
            current_taxi.drive(drive_distance)
            bill_to_date += current_taxi.get_fare()
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill_to_date:,.2f}")
        print(MENU)
        choice = input(">>> ").lower()


def display_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} {taxi}")


def get_valid_taxi_choice(taxis):
    is_valid = False
    while not is_valid:
        choice = input("Choose taxi: ")
        try:
            return taxis[int(choice)]
        except IndexError:
            print("Invalid taxi choice")
        except ValueError:
            print("Invalid taxi choice")
        is_valid = True


main()
