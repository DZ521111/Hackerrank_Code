'''
Author : Dhruv B Kakadiya

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(n, arr):
    # Write your code here
    sum1, sum2 = 0, 0 
    for i in range(n):
        sum1 += arr[i][i]
    k = n - 1
    for i in range(n):
        sum2 += arr[i][k]
        k -= 1
    return (abs(sum1 - sum2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
