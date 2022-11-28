"""
Band class
"""


class Band:
    """Band class for storing details of band"""

    def __init__(self, name: str):
        """Initialise a band"""
        self.name = name
        self.bands = []

    def __str__(self):
        """Return neatly formatted string."""
        return f"{self.name} ({self.bands[0]})"

    def add(self, member):
        """Add musician to band collection."""
        self.bands.append(member)
