'''
Author : Dhruv B Kakadiya

'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the plusMinus function below.
def plusMinus(arr):
    pc, nc, zc = 0, 0, 0
    for i in arr:
        if (i > 0):
            pc += 1
        elif (i < 0):
            nc += 1
        else:
            zc += 1
    return (pc/len(arr), nc/len(arr), zc/len(arr))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    a, b, c = plusMinus(arr)
    print(a)
    print(b)
    print(c)
