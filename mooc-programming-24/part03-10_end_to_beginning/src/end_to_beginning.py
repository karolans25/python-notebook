# Write your solution here
string = input("Please type in a string: ")

length = len(string)
counter = 1

while counter <= length:
    print(string[-1*counter])
    counter += 1
