import collections
if __name__ == '__main__':
    n, m = map(int,input().split())
    array_n = list(map(int, input().split()))
    set_A = set(map(int, input().split()))
    set_B = set(map(int, input().split()))
    temp = collections.Counter(array_n)
    set_C = set_A - set_B
    set_D = set_B - set_A
    happiness = 0
    for i in set_C:
        if temp[i]:
            happiness += temp[i]

    for i in set_D:
        if temp[i]:
            happiness -= temp[i]

    print(happiness)
