import random
import re

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
dict_words = {}
arr_words = words.split()

for i in range(0, len(arr_words) - 1):
    word = arr_words[i]
    next_word = arr_words[i+1]
    if word in dict_words:
        dict_words[word].append(next_word)
    else:
        dict_words[word] = [next_word]

# Get words that start with a capital letter
start_words = [word for word in dict_words.keys(
) if re.match(r'^\"?[A-Z]', word) is not None]
# Remove words that also end with end-of-sentence punctuation
start_words = [word for word in start_words if re.search(
    r'[\.\?!]\"?$', word) is None]

# Get words that end with end-of-sentence punctuation
stop_words = [word for word in dict_words.keys(
) if re.search(r'[\.\?!]\"?$', word) is not None]

# TODO: construct 5 random sentences
# Your code here


def rand_sentence():
    word = random.choice(start_words)
    print(word, end=" ")

    while word not in stop_words:
        next_word = random.choice(dict_words[word])
        print(next_word, end=" ")
        word = next_word


for i in range(0, 5):
    rand_sentence()
    print('\n')
