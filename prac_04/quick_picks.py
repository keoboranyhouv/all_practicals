
def main():
    import random
    random_number_per_line = 6
    begin = 1
    end = 45

    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks <= 0:
        print("Please enter valid picks")
        number_of_picks = int(input("How many quick picks? "))

    for pick in range(number_of_picks):
        quick_picks = []
        for number in range(random_number_per_line):
            random_number = random.randint(begin,end)
            while random_number in quick_picks:
                random_number = random.randint(begin, end)
            quick_picks.append(random_number)
        quick_picks.sort()
        print(" ".join("{:3}".format(number) for number in quick_picks))


if __name__ == '__main__':
    main()