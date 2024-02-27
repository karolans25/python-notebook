# Write your solution here
number = int(input("Please type in a number: "))

init = 1

while number > init:
    print(init)
    print(number)
    init += 1
    number -= 1

if init == number:
    print (init)