# https://www.hackerrank.com/challenges/mini-max-sum/problem

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
    new_arr = sorted(arr)
    min_sum = sum(new_arr[:4])
    max_sum = sum(new_arr[-4:])
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
