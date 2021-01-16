#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleDistance = []
    orangeDistance = []
    appleCounter, orangeCounter = 0, 0
    for i in apples:
        appleDistance.append(a + i)
    for i in appleDistance:
        if (s <= i <= t):
            appleCounter += 1 
    for j in oranges:
        orangeDistance.append(b + j)
    for j in orangeDistance:
        if (s <= j <= t):
            orangeCounter += 1
    print(appleCounter)
    print(orangeCounter)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
