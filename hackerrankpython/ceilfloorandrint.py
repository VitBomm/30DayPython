import numpy as np
np.set_printoptions(sign=' ')
arrayNumpy = np.array([x for x in map(float,input().split())])

print(np.floor(arrayNumpy))
print(np.ceil(arrayNumpy))
print(np.rint(arrayNumpy))
