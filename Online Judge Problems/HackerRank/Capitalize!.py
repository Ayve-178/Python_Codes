#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l = len(s)
    #x = ""
    for i in range(l):
        if i == 0:
            s = s[i].swapcase() + s[i+1:]
        elif s[i-1] == " " and (s[i]>='a' and s[i]<='z'):
            s = s[:i] + s[i].swapcase() + s[i+1:]
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
