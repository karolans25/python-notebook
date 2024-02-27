# Write your solution here
name = input("Please tell me your name: ")
cost_unit = 5.90

if name != 'Jerry':
    portions = int(input("How many portions of soup? "))
    total = portions * cost_unit
    print(f"The total cost is {total}")

print("Next please!")