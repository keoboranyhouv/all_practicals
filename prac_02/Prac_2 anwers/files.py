# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
out_file = open('name.txt', "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

# 2. Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).
in_file = open("name.txt", "r")
for name in in_file:
    print("Your name is {}".format(name))
in_file.close()

# 3. Create a text file called numbers.txt and save it in your prac_02 directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers
# and adds them together then prints the result, which should be... 59.

in_file = open('numbers.txt', 'r')
first_number = int(in_file.readline())
second_number = int(in_file.readline())
total = first_number + second_number
print(f"The total of the first 2 numbers is {total}")
in_file.close()

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt
# or a file with any number of numbers.

in_file = open('numbers.txt', 'r')
total = 0
try:
    for n in in_file:
        n.strip()
        number = int(n)
        total = total + number
except ValueError:
    print(f"The total of all numbers is {total}")
in_file.close()