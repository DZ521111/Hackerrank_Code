'''


'''

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    timeZone = s[-2:]
    if (timeZone == "PM"):
        if (s[:2] == "12"):
            return (s[:-2])
        else:
            hour = int(s[:2]) + 12
            s = str(hour) + s[2:]
            return (s[:-2])
    else:
        if (s[:2] == "12"):
            s = str("00") + s[2:]
        return (s[:-2])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
