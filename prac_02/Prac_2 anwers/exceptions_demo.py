"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# ANS: when either numerator or denominator is not an integer
2. When will a ZeroDivisionError occur?
# ANS: when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Cannot divide by Zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

