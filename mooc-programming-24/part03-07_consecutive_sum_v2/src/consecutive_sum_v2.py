# Write your solution here
number = int(input("Limit: "))
counter = 1
result = 0
response = ''

while result < number:
    result += counter
    response += f"{counter} + "
    counter += 1

print(f"The consecutive sum: {response[:-3]} = {result}")