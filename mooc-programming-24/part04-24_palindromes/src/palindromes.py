# Write your solution here
def palindromes(word):
    for i in range(len(word)//2):
        if word[i] != word[len(word) - i -1]:
            return False
    return True

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(f"{word} is a palindrome!")
        break
    print("that wasn't a palindrome")
