def main():
    try:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))

        result = number1 / number2

        print(f"{number1} / {number2} = {result}")

    except ValueError: # except cannot be too broad (general exception)
        print("Wrong entry: Must be integers!")

    except ZeroDivisionError:
        print("Second number must be a non-zero integer!")

    print()
    print("=== End of progress ===")


if __name__ == '__main__':
    main()
