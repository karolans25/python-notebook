# Write your solution here
number = int(input("Please type a number: "))
order = 1000

while number < order:
    print(f"This number is smaller than {order}");
    order //= 10

print("Thank you!")