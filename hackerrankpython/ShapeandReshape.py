import numpy

arr = input().strip().split(' ')
result = numpy.array(arr, int)
print(result.reshape(3,3))