# Write your solution here
number = int(input("Limit: "))
counter = 1
result = 0

while result < number:
    result += counter
    counter += 1

print(result)
