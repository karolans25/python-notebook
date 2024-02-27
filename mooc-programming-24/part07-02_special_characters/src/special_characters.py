# Write your solution here
def separate_characters(my_string: str):
    ascii_letters = ''
    punctuation = ''
    rest = ''
    for i in my_string:
        if i.isalnum() or i == ' ':
            if i.isascii() and i != ' ':
                ascii_letters += i
            else:
                rest += i
        else:
            punctuation += i
    return (ascii_letters, punctuation, rest)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])