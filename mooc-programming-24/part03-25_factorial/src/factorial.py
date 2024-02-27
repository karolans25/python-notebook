# Write your solution here
number = int(input("Please type in a number: "))
res = 1
count = number

while number > 0:
    while count > 1:
        res *= count
        count -= 1
    print (f"The factorial of the number {number} is {res}")
    number = int(input("Please type in a number: "))
    res = 1
    count = number

if number <= 0:
    print("Thanks and bye!")