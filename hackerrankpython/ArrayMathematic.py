import numpy as np

n, m = map(int,input().split())

Array_A = np.array([[x for x in map(int,input().split())] for _ in range(n)],int)
Array_B = np.array([[x for x in map(int,input().split())] for _ in range(n)],int)
print(np.add(Array_A, Array_B))
print(np.subtract(Array_A,Array_B))
print(np.multiply(Array_A, Array_B))
print(Array_A // Array_B)
print(np.mod(Array_A, Array_B))
print(np.power(Array_A, Array_B))