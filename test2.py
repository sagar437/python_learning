#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    #
    # Write your code here.
    #
    count = 0
    max_height = int(max(ar))
    for num in ar:
        if num == max_height:
            count = count + 1
    print(count)
            

if __name__ == '__main__':
#    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()

