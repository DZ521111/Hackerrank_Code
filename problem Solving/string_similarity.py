#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stringSimilarity function below.
def stringSimilarity(s):
    t = s + "$" + s
    l, r = 0, 0
    z = [0] * len(t)
    for i in range(len(t)):
        if(i > r):
            l = r = i
            while(r < len(t) and t[r] == t[r - l]):
                r += 1
            z[i] = r - l
            r -= 1
        else:
            i1 = i - l
            if(z[i1] < r - i + 1):
                z[i] = z[i1]
            else:
                l = i
                while(r < len(t) and t[r] == t[r - l]):
                    r += 1
                z[i] = r - l
                r -= 1
    print(z)
    return sum(z[len(s) + 1 : ])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
