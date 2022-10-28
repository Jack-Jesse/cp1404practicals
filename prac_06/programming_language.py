"""Programming Language"""


class ProgrammingLanguage:
    """Programming language object"""

    def __init__(self, language="", typing="", reflection="", year=0):
        """Initialise a ProgrammingLanguage instance"""

        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.language}, {self.typing}, {self.reflection}, {self.year}"

    def is_dynamic(self):
        return self.typing == "Static"
