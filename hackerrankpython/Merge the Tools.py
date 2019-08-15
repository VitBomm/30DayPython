def merge_the_tools(string, k):
    i = 0
    index = k
    substring_arr = []

    while(index <= len(string)):
        substring_arr.append(string[i:index])
        i += k
        index += k

    for i in substring_arr:
        print(''.join(list(dict.fromkeys(i))))



if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
