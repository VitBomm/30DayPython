import numpy as np
np.set_printoptions(sign=' ')
n, m = map(int,input().split())
my_array = np.array([[x for x in map(float,input().split())] for _ in range(n)])
print(np.mean(my_array, axis=1))
print(np.var(my_array, axis=0))
print('{0}'.format(round(np.std(my_array),12)))