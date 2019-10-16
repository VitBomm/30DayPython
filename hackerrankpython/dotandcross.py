import numpy as np

n = int(input())

arrayA = np.array([[x for x in map(int,input().split())] for _ in range(n)])
arrayB = np.array([[x for x in map(int,input().split())] for _ in range(n)])

print(np.dot(arrayA, arrayB))


