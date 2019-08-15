def count_substring(string, sub_string):
    i = 0
    count = 0
    len_sub =len(sub_string)
    for _ in range(len(string) - len_sub +1):
        if string[i:len_sub] == sub_string:
            count += 1
        i += 1
        len_sub += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
