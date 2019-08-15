def mutate_string(string, position, character):
    listtemp = list(string)
    listtemp[position] = character
    return ''.join(listtemp)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
