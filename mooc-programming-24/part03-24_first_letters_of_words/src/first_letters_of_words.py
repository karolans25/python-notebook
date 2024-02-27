# Write your solution here
sentence = input("Please type in a sentence: ")

words = sentence.split(" ")

while len(words) > 0:
    print(words[0][0])
    words.pop(0)