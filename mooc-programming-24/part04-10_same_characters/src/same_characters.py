# Write your solution here
def same_chars(text, index_1, index_2):
    if index_1 >= len(text) or index_2 >= len(text):
        return False
    return text[index_1] == text[index_2]

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))