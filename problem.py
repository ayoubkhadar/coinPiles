#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'coinPiles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def coinPiles(n, arr):
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Write your code here

    x = int(raw_input().strip())

    n = int(raw_input().strip())

    arr = map(int, raw_input().rstrip().split())

    results = coinPiles(n, arr)

    fptr.write(str(results) + '\n')

    fptr.close()
