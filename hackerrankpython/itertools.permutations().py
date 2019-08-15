from itertools import permutations
s, k = input().split()
k = int(k)
s = list(s)
for a in sorted(list(permutations(s,k))):
    print(''.join(list(a)))
