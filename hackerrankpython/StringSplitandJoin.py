def split_and_join(line):
    # write your code here
    temp = ''
    for _ in line:
        if(_ == ' '):
            temp += '-'
        else:
            temp += _
    return temp

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
