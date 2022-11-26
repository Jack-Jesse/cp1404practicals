"""
Silver service taxi class
Estimate: 60 minutes
10 minutes so far
Actual:
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """SilverServiceTaxi class for storing SilverServiceTaxi details."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness: float):
        """Initialise SilverServiceTaxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return neatly formatted string."""
        return f"{super().__str__()}, flagfall of ${self.flag_fall:,.2f}"

    def get_fare(self):
        """Get the fare"""
        fare = round(self.flag_fall + super().get_fare(), 1)
        return fare


