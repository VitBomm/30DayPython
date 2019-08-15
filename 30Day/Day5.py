#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    for i in range(10):
        print("{0} x {1} = {2}".format(n,i+1,n*(i+1)))
