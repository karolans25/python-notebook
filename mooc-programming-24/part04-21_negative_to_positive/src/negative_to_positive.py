# Write your solution here
limit = 0

while limit <= 0:
    limit = int(input("Please type in a positive integer: "))
    if limit <= 0:
        print("Write a positvie number")

for i in range(-1*limit, limit + 1):
    if i != 0:
        print(i)