# Write your solution here
def anagrams (text_1, text_2):
    return sorted(text_1) == sorted(text_2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False