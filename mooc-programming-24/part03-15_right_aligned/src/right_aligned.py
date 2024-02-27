# Write your solution here
string = input("Please type in a string: ")

if len(string) > 20:
    print("Only accepted a string with length of 20 characters")
else:
    print(f"{'*'*(20-len(string))}{string}")