from math import sqrt
# Write your solution here
number = int(input("Please type in a number: "))

while number != 0:
    if number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))
    number = int(input("Please type in a number: "))

print("Exiting...")