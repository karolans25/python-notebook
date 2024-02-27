# Write your solution here
word = input("Please type in a string: ")

# if word.find('a') != -1:
#     print('a found')
# else:
#     print('a not found')
# 
# if word.find('e') != -1:
#     print('e found')
# else:
#     print('e not found')
# 
# if word.find('o') != -1:
#     print('o found')
# else:
#     print('o not found')

vowels = 'aeo'
index = 0

while index < len(vowels):
    if vowels[index] in word:
        print(f"{vowels[index]} found")
    else:
        print(f"{vowels[index]} not found")
    index += 1
