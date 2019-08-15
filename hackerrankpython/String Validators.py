if __name__ == '__main__':
    n = input()
    is_alnum = False
    is_alpha = False
    is_digit = False
    is_lower = False
    is_Upper = False
    for _ in list(n):
        if is_alnum == False and _.isalnum():
            is_alnum = True
        if is_alpha == False and _.isalpha():
            is_alpha = True
        if is_digit == False and _.isdigit():
            is_digit = True
        if is_lower == False and _.islower():
            is_lower = True
        if is_Upper == False and _.isupper():
            is_Upper = True

    print("{0}\n{1}\n{2}\n{3}\n{4}".format(is_alnum,is_alpha, is_digit, is_lower, is_Upper))
