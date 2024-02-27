# Write your solution here
number = int(input("Please type in a number: "))

first = 1
second = 1

while first <= number and second <= number:
    print(f"{first} x {second} = {first * second}")
    if second != number:
        second += 1
    else:
        first += 1
        second = 1