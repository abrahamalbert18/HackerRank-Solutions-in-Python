#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minimum = 9999999999
    maximum = 0
    total = 0
    for i in arr:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
        total += i

    minimumSum = total - maximum
    maximumSum = total - minimum
    print(minimumSum, maximumSum)
    pass


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
