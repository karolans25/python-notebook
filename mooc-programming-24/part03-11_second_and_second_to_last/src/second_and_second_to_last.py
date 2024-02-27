# Write your solution here
string = input("Please type in a string: ")

if len(string) >= 2:
    if string[1] == string [-2]:
        print(f"The second and the second to last characters are {string[1]}")
    else:
        print("The second and the second to last characters are different")
else:
    print("Type in a string with at least two letters")