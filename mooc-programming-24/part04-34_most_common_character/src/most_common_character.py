# Write your solution here
def most_common_character(text):
    letter = text[0]
    for i in text:
        if text.count(i) > text.count(letter):
            letter = i
    return letter

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))