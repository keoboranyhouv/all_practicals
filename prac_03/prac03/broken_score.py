import random


def main():
    score = float(input("Enter score: "))
    result = generate_results(score)
    print(f"Result: {result}")

    random_score = random.randint(0,100)
    print("Random score:",random_score)
    random_result = generate_results(random_score)
    print(f"Result: {random_result}")


def generate_results(score):
    if 0 <= score <= 100:
        if score >= 90:
            return "Excellent"
        elif score >= 50:
            return "Passable"
        else:
            return "Bad"
    else:
        return "Invalid score!"


if __name__ == '__main__':
    main()
