# Write your solution here
word = input("Please type in a word: ")
text = input("Please type in a character: ")

index = word.find(text)

if index == -1:
    # print("The substring does not occur once in the string.")
    print("The substring does not occur twice in the string.")
else:
    index2 = word[index + len(text) : ].find(text)
    if index2 == -1:
        print("The substring does not occur twice in the string.")
    else: 
        print(f"The second occurrence of the substring is at index {index + index2 + len(text)}.")