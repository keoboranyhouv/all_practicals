MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)


choice = input(">>> ").upper()


def convert_celsius_to_fahrenheit():
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius():
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_celsius_to_fahrenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_fahrenheit_to_celsius()
        print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
