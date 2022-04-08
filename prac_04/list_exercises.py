def main():
    """Get 5 numbers and display details"""
    numbers = []
    for number in range(0, 5):
        input_number = int(input("Number: "))
        numbers.append(input_number)

    print(f"The first number is {print_first_number(numbers)} ")
    print(f"The last number is {print_last_number(numbers)}")
    print(f"The smallest number is {print_smallest_number(numbers)}")
    print(f"The largest number is {print_largest_number(numbers)}")
    print(f"The average of the numbers is {print_average_number(numbers)}")

    # Check if the username in the list
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")



def print_average_number(numbers):
    average_number = sum(numbers) / len(numbers)
    return average_number


def print_largest_number(numbers):
    largest_number = max(numbers)
    return largest_number


def print_smallest_number(numbers):
    smallest_number = min(numbers)
    return smallest_number


def print_last_number(numbers):
    last_number = numbers[-1]
    return last_number


def print_first_number(numbers):
    first_number = numbers[0]
    return first_number


if __name__ == '__main__':
    main()