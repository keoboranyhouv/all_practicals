# for statement
for i in range(10):
    if i % 2 != 0: # if i divided 2's remainder is not ZERO
        continue # skip the rest of the statements
    print(i)

for i in range(10):
    if i % 2 == 0:
        print(i)

# range
numbers = range(10) # from 0 to 10 (excluded 10)
print(numbers)

for i in range(5): # 0,1,2,3,4
    print(i)

for j in range(2,6): # always excluded the last one
    print(j)

for k in range(1, 20, 3): # 1,4,7,10,13,16,19
    print(k)

# while
score = int(input("Enter score: "))
while score < 0 or score > 10:
    print("Invalid range!")
    score = int(input("Enter score: "))
print("You entered: ", score)
if score >= 5:
    print("You passed")
else:
    print("You failed")
choice = input("Do you wish to continue? y/n")






