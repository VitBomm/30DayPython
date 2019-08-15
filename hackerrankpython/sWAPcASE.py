def swap_case(s):
    a = ''
    for _ in s:
        if _.isupper():
            a += _.lower()
        elif _.islower():
            a += _.upper()
        else:
            a += _
    return a

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
