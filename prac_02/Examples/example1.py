def main():
    expenses = []

    in_file = open("expenses.txt") # store the amount(s) into a list
    in_file.readline()  # throw away the header
    for line in in_file.readline():
        expense_data = line.split()
        for i in range(1, len(expense_data)): # exclude column 0
            expense_data[i] = float(expense_data[i]) # convert to float
       # print(expense_data)  for debugging purpose
        expenses.append(expense_data)

    in_file.close()
    # use the list for calculation purposes
    print(expenses)
    total_expenses = 0
    for expense in expenses:
        for i in range(1, len(expense)):
            total_expenses += expense[i]
    print("Total spent: $", total_expenses)


if __name__ == '__main__':
    main()