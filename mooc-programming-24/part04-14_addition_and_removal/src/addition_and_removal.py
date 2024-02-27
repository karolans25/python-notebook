# Write your solution here
result = []

while True:
    print(f"The list is now {result}")
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option.lower() == 'd':
        result.append(len(result) + 1)
    elif option.lower() == 'r' and len(result) > 0:
        result.remove(len(result))
    elif option.lower() == 'x':
        break

print("Bye!")