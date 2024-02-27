# Write your solution here
string_1 = input("Please type in string 1: ")
string_2 = input("Please type in string 2: ")

len_1 = len(string_1)
len_2 = len(string_2)

if len_1 > len_2:
    print(string_1 + " is longer")
elif len_2 > len_1:
    print(string_2 + " is longer")
else:
    print("The strings are equally long")