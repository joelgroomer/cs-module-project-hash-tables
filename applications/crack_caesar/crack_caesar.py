# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
import re

ciphertext = ""
frequency = {}
key = {}
known_freq_order = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
                    'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# open the file with the encrypted text
with open("ciphertext.txt", "r") as f:
    while True:
        # read one character at a time until empty string is found (EOF)
        cipher_char = f.read(1)
        if cipher_char == "":
            break

        ciphertext += cipher_char   # this will hold the entire encrypted file
        if re.match(r'[A-Z]', cipher_char) is not None:
            # add each alpha character to the frequency dictionary
            # and track frequency
            if cipher_char in frequency:
                frequency[cipher_char] += 1
            else:
                frequency[cipher_char] = 1

# sort characters by frequency, highest first
cipher_char_freq = sorted(
    frequency.items(), key=lambda tup: tup[1], reverse=True)

# just in case the cypher text doesn't use all 26 characters,
# reduce the times the loop will run
max = 26
if len(ciphertext) < 26:
    max = len(ciphertext)

# loop through the characters and make a `key` dictionary
# matching the characters by frequency to the known frequency
# of characters in the English language
for i in range(0, max):
    key[cipher_char_freq[i][0]] = known_freq_order[i]


# decrypt character by character
decoded = ""
for char in ciphertext:
    if re.match(r'[A-Z]', char) is not None:
        decoded += key[char]
    else:
        decoded += char

print(decoded)
