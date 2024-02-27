# Write your solution here
numbers = [1, 2, 3, 4, 5]

index = 0

while index != -1:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index > len(numbers):
        print("Index out of range")
        continue
    value = int(input("new value: "))
    numbers[index] = value
    print(numbers)