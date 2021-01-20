#!/bin/python3

import math
import os
import random
import re
import sys

def find_morgen(a, b):
    a += 'z'
    b += 'z'

    for i in range(len(a) + len(b) - 2):
        if (a < b):
            yield a[0]
            a = a[1 : ]
        else:
            yield b[0]
            b = b[1 : ]

def morganAndString(a, b):
    return (''.join(find_morgen(a, b)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()
