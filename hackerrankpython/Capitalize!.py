#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    a = s.split(' ')
    z = []
    for _ in a:
        if len(_) == 1:
            z.append(_.upper())
        else:
            z.append(_.capitalize())
    return ' '.join(z)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
