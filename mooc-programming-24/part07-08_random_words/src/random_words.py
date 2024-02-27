# Write your solution here
from random import sample

def words(n: int, beginning: str):
    list_words = []
    with open("words.txt") as file:
        for line in file:
            if line.startswith(beginning):
                list_words.append(line.replace('\n', ''))
    
    return sample(list_words, n)

if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)