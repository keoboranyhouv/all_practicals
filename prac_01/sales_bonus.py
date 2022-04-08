"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
EXIT = -1
sales = float(input("Enter sales or -1 to exit: $"))
while sales != -1:
    if sales < 1000:
        bonus = int(sales * 0.1)
    else:
        bonus = int(sales * 0.15)
    print("Your bonus is: {}".format(bonus))
    sales = float(input("Enter sales: $"))



