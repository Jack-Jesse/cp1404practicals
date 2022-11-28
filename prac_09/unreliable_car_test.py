"""
Unreliable Car Test
For testing the UnreliableCar.
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("1960 Car", 50, 50.0)
    print(unreliable_car)
    unreliable_car.drive(50)
    print(unreliable_car)


main()
