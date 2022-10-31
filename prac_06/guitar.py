"""
Guitar Class
CP1404/CP5632 Practical
Estimate: 45 minutes
Actual: 30 minutes
"""


class Guitar:
    """Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise guitar instance."""

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return neatly formated string for printing."""
        return f"My guitar {self.name} first made in {self.year} costs: ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of guitar"""
        return 2022 - self.year

    def is_vintage(self):
        return self.get_age() >= 50
