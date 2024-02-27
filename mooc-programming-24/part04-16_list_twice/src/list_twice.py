# Write your solution here
result = []
while True:
    number = int(input("New item: "))
    if number == 0:
        break
    result.append(number)
    print(f"The list now: {result}")
    print(f"The list in order: {sorted(result)}")

print("Bye!")