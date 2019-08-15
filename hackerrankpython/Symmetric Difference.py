if __name__ == '__main__':
    n = input()
    arr1 = set(map(int, input().split()))
    m = input()
    arr2 = set(map(int, input().split()))
    temp = (set(arr1.difference(arr2)) | set(arr2.difference(arr1)))

    for i in sorted(temp):
        print(i)
