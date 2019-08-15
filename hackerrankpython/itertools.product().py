from itertools import product

a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(' '.join("({}, {})".format(a,b) for a,b in list(product(a, b))))

