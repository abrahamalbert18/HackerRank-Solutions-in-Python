#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0
    zeros = 0
    lengthOfArray = len(arr)
    for i in arr:
        if i > 0:
            positives += 1
        elif i < 0:
            negatives += 1
        else:
            zeros += 1

    positiveRatios = positives / lengthOfArray
    negativeRatios = negatives / lengthOfArray
    zeroRatios = zeros / lengthOfArray
    print(round(positiveRatios, 6))
    print(round(negativeRatios, 6))
    print(round(zeroRatios, 6))
    pass


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
