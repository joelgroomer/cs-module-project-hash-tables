def word_count(s):
    # Your code here
    counts = {}

    s = s.replace('"', '').replace(':', '').replace(';', '').replace(',', '')
    s = s.replace('.', '').replace('-', '').replace('+', '').replace('=', '')
    s = s.replace('/', '').replace('\\', '').replace('|', '').replace('[', '')
    s = s.replace(']', '').replace('{', '').replace('}', '').replace('(', '')
    s = s.replace(')', '').replace('*', '').replace('^', '').replace('&', '')
    s = s.lower()
    arr = s.split()
    for word in arr:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
