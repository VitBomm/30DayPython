import numpy as np
n, m = map(int, input().split())
matrix = np.array([[x for x in map(int, input().split())]for y in range(n)])
print(np.transpose(matrix))
print(matrix.flatten())

