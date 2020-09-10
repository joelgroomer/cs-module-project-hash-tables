def no_dups(s):
    # Your code here
    final = []
    arr = s.split()

    for word in arr:
        if word not in final:
            final.append(word)

    str_final = ''
    for word in final:
        str_final += word + ' '

    return str_final.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
