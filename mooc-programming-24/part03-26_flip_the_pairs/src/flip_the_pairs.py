# Write your solution here
number = int(input("Please type in a number: "))

init = 2

while init <= number:
    print(init)
    print(init-1)
    init += 2

if number % 2 == 1:
    print(number)