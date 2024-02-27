# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
quantity = 0
add = 0
positives = 0

while True:
    number = int(input("Number: "))
    if number == 0:
        break
    quantity += 1
    add += number
    if number > 0:
        positives += 1

if quantity != 0:
    print(f"Numbers typed in {quantity}")
    print(f"The sum of the numbers is {add}")
    print(f"The mean of the numbers is {add / quantity}")
    print(f"Positive numbers {positives}")
    print(f"Negative numbers {quantity - positives}")
else:
    print("Write at least one number different to 0")