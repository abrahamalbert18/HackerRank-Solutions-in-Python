#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    militaryTime = ""
    isAM = s[-2:] == "AM"

    if isAM:
        if s[:2] == "12":
            militaryTime += "00"
        else:
            militaryTime += s[:2]
    else:
        if int(s[:2]) == 12:
            militaryTime += "12"
        else:
            militaryTime += str(int(s[:2]) + 12)

    militaryTime += s[2:-2]
    return militaryTime


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
