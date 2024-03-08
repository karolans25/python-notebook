# WRITE YOUR SOLUTION HERE:
from string import punctuation as pct

def most_common_words(filename: str, lower_limit: int):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.replace('\n', ' ') + ' '
        for mark in pct:
            text = text.replace(mark, '')
        return {w: text.count(' ' + w + ' ') for w in text.split(' ') if text.count(' ' + w + ' ') >= lower_limit}

if __name__ == '__main__':
    print(most_common_words("comprehensions.txt", 3))
