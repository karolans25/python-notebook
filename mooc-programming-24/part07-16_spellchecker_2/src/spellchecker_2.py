# write your solution here
from difflib import get_close_matches as gcmatch

words_file = "wordlist.txt"
words = []
mispelled = []

# Read word file
with open(words_file) as new_file:
    for line in new_file:
        line = line.replace('\n', '').strip()
        words.append(line.lower())
    
text = input("Write text: ")
text_words = text.split(' ')
for word in text_words:
    if word.lower() in words:
        print(f"{word} ", end='')
    else:
        print(f"*{word}* ", end='')
        mispelled.append(word)

print()
print('suggestions:')
for word in mispelled:
    print(f"{word}: ", end='')
    print(', '.join(gcmatch(word, words, n=3, cutoff=0.6)))
