# Write your solution here
word = input("Please type in a string: ")

length = len(word)
counter = 1

while counter <= length:
    print(word[:counter])
    counter += 1