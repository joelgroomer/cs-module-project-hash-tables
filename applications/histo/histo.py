# Your code here
from operator import itemgetter

with open("robin.txt") as f:
    text = f.read()

text = text.replace('"', '').replace(':', '').replace(';', '').replace(',', '')
text = text.replace('.', '').replace('-', '').replace('+', '').replace('=', '')
text = text.replace('/', '').replace('\\',
                                     '').replace('|', '').replace('[', '')
text = text.replace(']', '').replace('{', '').replace('}', '').replace('(', '')
text = text.replace(')', '').replace('*', '').replace('^', '').replace('&', '')
text = text.replace('?', '').replace('!', '')
text = text.lower()
words = text.split()

word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

alphabetized = sorted(word_counts.items(), key=itemgetter(0), reverse=False)
ordered = sorted(alphabetized, key=itemgetter(1), reverse=True)

for tup in ordered:
    tabs = 3
    if len(tup[0]) >= 8:
        tabs -= 1
    if len(tup[0]) >= 16:
        tabs -= 1

    print(tup[0], end=("\t" * tabs))
    for i in range(0, tup[1]):
        print("#", end="")
    print(f" ({tup[1]})")
