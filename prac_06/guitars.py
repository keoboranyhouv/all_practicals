from guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        pending_guitar = Guitar(name, year, cost)
        guitars.append(pending_guitar)
        print(pending_guitar, "added.")
        name = input("Name: ")

    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars):
            vintage_status = ""
            if guitar.is_vintage():
                vintage_status = "(vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f} {2}".format(i + 1, guitar, vintage_status))
    else:
        print("No guitars!")


main()
