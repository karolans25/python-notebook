# Write your solution here
word = input("Please type in a word: ")
letter = input("Please type in a character: ")

index = word.find(letter)

while index != -1 and len(word) >= (index+3):
    print(word[index: index+3])
    word = word[index+1:]
    index = word.find(letter)
    
