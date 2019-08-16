#Day 16: Exceptions - String to Integer

# Task 
# Read a string,S, and print its integer value; if S cannot be converted to an integer, print Bad String.

import sys


S = input().strip()
try:
    int(S)
    print(S)
except ValueError:
    print("Bad String")


