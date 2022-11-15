"""
Convert miles to km
CP1404/CP5632 Practical
Estimate: 30 minutes 11:13am
Actual:
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesToKm(App):
    """Initialise class for Convert to miles to kilometres program."""
    message = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file("convert_miles_km.kv")
        self.message = "Type in a number"
        return self.root

    def handle_up(self):
        """Handle the up button press."""
        user_input_number = int(self.root.ids.user_input.text)
        self.root.ids.user_input.text = str(user_input_number + 1)

    def handle_down(self):
        """Handle the down button press."""
        user_input_number = int(self.root.ids.user_input.text)
        self.root.ids.user_input.text = str(user_input_number - 1)

    def handle_convert(self):
        """Handle the convert button press miles to kilometres."""
        kilometres = int(self.root.ids.user_input.text) * 1.609
        self.message = str(kilometres)


ConvertMilesToKm().run()
