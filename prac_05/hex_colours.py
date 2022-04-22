CODE_TO_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Aliceblue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "Antiquewhite2": "#eedfcc"}

colour_name = input("Enter Colour: ").title()
while colour_name != "":
    if colour_name in CODE_TO_COLOUR:
        print(CODE_TO_COLOUR[colour_name])
    else:
        print("Invalid colour!")
    colour_name = input("Enter Colour: ").title()
