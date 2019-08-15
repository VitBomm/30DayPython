from collections import defaultdict

dictionary = defaultdict(list)

n, m = map(int, input().split())

for i in range(n):
    arg = input()
    dictionary[arg].append(str(i+1))

for j in range(m):
    arg = input()
    if len(dictionary[arg]) == 0:
        print("-1")
    else:
        print(" ".join(dictionary[arg]))
