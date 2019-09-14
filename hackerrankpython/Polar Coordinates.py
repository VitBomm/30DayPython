from cmath import phase,polar
import math
a = input()

b = polar(complex(a))
print("{0:.3f}\n{1:.3f}".format(b[0],b[1]))