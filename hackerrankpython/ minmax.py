import numpy as np

m, n = map(int,input().split())

Array = np.array([[x for x in map(int,input().split())] for _ in range(n)])

print(np.max(np.min(Array,axis=1)))
