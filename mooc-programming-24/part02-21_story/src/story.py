# Write your solution here
word = input("Please type in a word: ")
sentence = ''

while word != 'end' and sentence.find(' ' + word + ' ') == -1:
#while word != 'end':
    sentence += f"{word} "
    word = input("Please type in a word: ")

print(sentence)