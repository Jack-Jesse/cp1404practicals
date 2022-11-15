"""
Convert miles to km
CP1404/CP5632 Practical
Estimate: 30 minutes 11:13am
Actual:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KILOMETRES = 1.609


class ConvertMilesToKm(App):
    """Initialise class for Convert to miles to kilometres program."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = "Type in a number"
        return self.root

    def handle_increment(self, change):
        """Handle the increment."""
        miles = int(self.get_valid_miles()) + change
        self.root.ids.user_input.text = str(miles)
        self.handle_convert()

    def handle_convert(self):
        """Handle the convert button press miles to kilometres."""
        miles = self.get_valid_miles()
        kilometres = int(miles) * MILES_TO_KILOMETRES
        self.message = str(kilometres)

    def get_valid_miles(self):
        """Get valid miles."""
        try:
            user_input = float(self.root.ids.user_input.text)
            return user_input
        except ValueError:
            return 0


ConvertMilesToKm().run()
