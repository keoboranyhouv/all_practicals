number_of_items = int(input("Number of items: "))
total_price = 0
DISCOUNT_RATE = 0.1

while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

    for item in range(number_of_items):
        price = float(input("Price of item: "))
        total_price = total_price + price

    if total_price >= 100:
        discount = total_price * DISCOUNT_RATE
        final_total = total_price - discount
        print("Total price for {} items is ${:.2f}".format(number_of_items,final_total))


