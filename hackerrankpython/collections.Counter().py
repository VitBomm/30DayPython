from collections import Counter
X = input()
shoes_size = list(map(int,input().split()))
n_customer = int(input())

newlist = Counter(shoes_size)
total = 0
for i in range(n_customer):
    a, b = map(int, input().split())
    if newlist[a] and newlist[a] != 0:
        total += b
        newlist[a] -= 1

print(total)
