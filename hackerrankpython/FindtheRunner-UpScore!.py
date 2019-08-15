if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = list(set(arr))
    list.sort(reverse = True)
    print(list[1])
