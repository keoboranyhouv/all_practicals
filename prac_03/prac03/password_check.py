
MIN_LENGTH = 10


def main():
    """Program to get and check a user's password."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    while not is_valid_password(password):
        print("*" * len(password))
        password = input("> ")


def get_password():
    print("Please enter a password")
    password = input("> ")
    return password


def is_valid_password(password):
    """Determine if the provided password is valid."""
    password_length = len(password)
    if password_length < MIN_LENGTH:
        return False

    return True


main()
