#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    if N %2 != 0 or N in range(6,21):
        print("Weird")
    elif N in range(2,6) or N >20:
        print("Not Weird")

