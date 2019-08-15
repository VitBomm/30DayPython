#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
# Complete the time_delta function below.
def preprocess_str(utc):
    value = int(utc[1:3]) * 3600 + int(utc[3:5]) * 60
    if utc[0] == '-':
        return value
    else:
        return -value

def time_delta(date_1, date_2 , utc_1, utc_2):
    date_3 = date_1 - date_2
    result = date_3.total_seconds() + (utc_1 - utc_2)
    if result > 0:
        return str(int(result))
    else:
        return str(int(-result))
if __name__ == '__main__':
    fptr = open("output.txt","+a")
    t = int(input())
    dict_month = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    for t_itr in range(t):
        #Sun 10 May 2015 13:54:36 -0700
        t1 = input().split()
        h,m,s = map(int,t1[-2].split(':'))
        utc_1 = preprocess_str(t1[-1])
        date_1 = datetime(int(t1[3]),dict_month[t1[2]],int(t1[1]),h,m,s)

        t2 = input().split()
        h,m,s = map(int,t2[-2].split(':'))
        utc_2 = preprocess_str(t2[-1])
        date_2 = datetime(int(t2[3]),dict_month[t2[2]],int(t2[1]),h,m,s)

        delta = time_delta(date_1, date_2, utc_1, utc_2)

        fptr.write(delta + '\n')

    fptr.close()
