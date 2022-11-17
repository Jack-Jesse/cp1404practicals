"""
unreliable car class
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of Car class for storing UnreliableCar information."""

    def __init__(self, name: str, fuel: int, reliability: float):
        """Initialise UnreliableCar class, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Print information in neatly formatted string."""
        return f"{super().__str__()}, {self.reliability}"

    def drive(self, distance):
        """Drive the unreliable car if random float is < reliability."""
        if random.uniform(1, 100) >= self.reliability:
            distance = 0
        return super().drive(distance)




