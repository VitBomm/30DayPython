import numpy as np
NP = []
MP = []
N, M, P = map(int,input().split())
[NP.append([x for x in map(int,input().split())]) for _ in range(N)]
[MP.append([x for x in map(int,input().split())]) for _ in range(M)]

print(np.concatenate((NP, MP), axis=0))