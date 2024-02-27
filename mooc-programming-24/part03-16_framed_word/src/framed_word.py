# Write your solution here
word = input("Word: ")

spaces = (28 - len(word))//2

print('*' * 30)
if len(word) % 2 == 0:
    print('*' + spaces * ' ' + word + spaces * ' ' +'*')
else:
    print('*' + spaces * ' ' + word + (spaces + 1) * ' ' +'*')
print('*' * 30)