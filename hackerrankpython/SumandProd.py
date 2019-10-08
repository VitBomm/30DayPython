import numpy as np
n, m = map(int,input().split())
array = np.array([[x for x in map(int,input().split())] for _ in range(n)])

print(np.prod(np.sum(array,axis=0)))



