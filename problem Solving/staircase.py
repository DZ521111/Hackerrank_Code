'''
Author : Dhruv B Kakadiya

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    k = n - 1
    for i in range(1, n + 1):
        print(" " * (k) + "#" * (i))
        k -= 1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
