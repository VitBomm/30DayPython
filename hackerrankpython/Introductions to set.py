def average(array):
    set_temp = set(array)
    return sum(set_temp) / len(set_temp)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
