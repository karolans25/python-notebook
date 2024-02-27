# Write your solution here
word = input("Please type in a word: ")
letter = input("Please type in a character: ")

index = word.find(letter)

if (len(word) >= (index+3)):
    print(word[index: index+3])