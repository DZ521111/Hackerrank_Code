'''
Author : Dhruv B Kakadiya

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_ = min_ = scores[0]
    mostTime, leastTime = 0, 0
    for i in scores[1:]:
        if (i > max_):
            max_ = i
            mostTime += 1
        elif (i < min_):
            min_ = i
            leastTime += 1
        else:
            continue
    return ([mostTime, leastTime])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
