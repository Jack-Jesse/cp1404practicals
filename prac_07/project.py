class Project:
    """Represent Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise Project instance"""

        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"name {self.name}, start_date {self.start_date}, priority {self.priority}, " \
               f"cost_estimate {self.cost_estimate} completion_percentage {self.completion_percentage}"
