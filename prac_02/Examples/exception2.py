def main():

    valid_input = False

    while not valid_input:
        try:
            age = int(input("Age?: "))
            # at this line, age is a valid
            if age >= 0:
                valid_input = True
            else:
                print("Please key in a positive number!")
        except ValueError:
            print("Age must be an integer!")

    print(f"You will be {age+10} in 10 years' times")


if __name__ == '__main__':
    main()