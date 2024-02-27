# Write your solution here
quantity = int(input("How many items: "))
result = []

while len(result) < quantity:
    number = int(input(f"Item {len(result) + 1}: "))
    result.append(number)

print(result)