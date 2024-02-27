# Write your solution here
number_1 = int(input("Please type in the first number: "))
number_2 = int(input("Please type in the second number: "))

if number_1 > number_2:
    print(f"The greater number was: {number_1}")
elif number_2 > number_1:
    print(f"The greater number was: {number_2}")
else:
    print("The numbers are equal!")