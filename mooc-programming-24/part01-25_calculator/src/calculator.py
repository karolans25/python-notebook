# Write your solution here
number_1 = int(input("Number 1: "))
number_2 = int(input("Number 2: "))
operation = input("Operation: ")

if(operation == 'add'):
    print(f"{number_1} + {number_2} = {number_1 + number_2}")
elif(operation == 'multiply'):
    print(f"{number_1} * {number_2} = {number_1 * number_2}")
elif(operation == 'subtract'):
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
