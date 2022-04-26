def main():

    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        acceptance = input(f'Is your name {name}? (y/n)').lower()
        if acceptance != "y" and acceptance != "":
            name = input('Name: ')
        email_to_name[email] = name
        email = input("Email: ")
    for email, name in email_to_name.items():
        print(f"{name:15} ({email})")


def extract_name_from_email(email):
    designation = email.split('@')[0]
    parts = designation.split('-')
    name = ' '.join(parts).title()
    return name


if __name__ == '__main__':
    main()