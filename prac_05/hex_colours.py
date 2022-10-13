"""
Hex Colours
CP1404/CP5632 Practical
Get colour from user then print the corresponding hex code.
"""

COLOUR_TO_HEX_CODE = {"Blue": "#0000ff", "Green": "#00ff00", "Black": "#000000", "Red": "#ff0000",
                      "Orange": "#ffa500", "Purple": "#551a8b", "Gray": "#bebebe", "Pink": "#ff1493",
                      "Yellow": "#ffff00", "Gold": "#b8860b"}

colour = input("Enter colour: ").title()
while colour != "":
    try:
        print(COLOUR_TO_HEX_CODE[colour])
    except KeyError:
        print("Colour not found")
    colour = input("Enter colour: ").title()
