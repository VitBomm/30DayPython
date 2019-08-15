def minion_game(string):
    len_string = len(string)
    vowels = ['U', 'E', 'O', 'A', 'I']
    stuart = 0
    kevin = 0
    index = 0
    for i in string:
        if i in vowels:
            kevin += (len_string - index)
        else:
            stuart += (len_string - index)
        index +=1
    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print("Kevin {0}".format(kevin))
    else:
        print("Stuart {0}".format(stuart))


if __name__ == '__main__':
    s = input()
    minion_game(s)
