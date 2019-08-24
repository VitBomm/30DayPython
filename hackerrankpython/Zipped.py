import statistics
import numpy as np
N, X = input().split()
zip1 = [list(map(float,input().split())) for _ in range(int(X))]
array = list(zip(*zip1))
for i in range(int(N)):
    print(round(statistics.mean(array[i]),1))