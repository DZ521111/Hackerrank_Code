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
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    seaLevel, totalValley = 0, 0
    for step in path:
        if (step is "U"):
            seaLevel += 1
        else:
            seaLevel -= 1
        if (step is "U" and seaLevel is 0):
            totalValley += 1
    return (totalValley)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
