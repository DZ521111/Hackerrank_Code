#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    roundG = []
    for g in grades:
        if (g < 38):
            roundG.append(g)
        else:
            mainG = g
            for i in range(1, 4):
                if ((g + i) % 5 == 0 and i < 3):
                    roundG.append(g + i)
                    break
            else:
                roundG.append(mainG)
    return roundG

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
