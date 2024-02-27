# Write your solution here
def no_vowels(text):
    vowels = 'aeiou'
    result = ''
    for i in text:
        if i.lower() not in vowels:
            result += i
    return result


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))