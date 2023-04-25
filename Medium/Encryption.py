# https://www.hackerrank.com/challenges/encryption/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    new_s = s.replace(" ", "")
    length = len(s)
    row = math.floor(math.sqrt(length))
    columns = math.ceil(math.sqrt(length))
    arr_matrix = []
    res = ""
    start = 0
    for i in range(row):
        x = []
        for j in range(columns):
            x.append(new_s[start])
            if new_s[start] == new_s[-1]:
                break
            else:
                start += 1
        arr_matrix.append(x)
    index = 0
    for i in range(columns):
        for j in range(row):
            res += arr_matrix[j][i]
            if arr_matrix[j][i] == new_s[-1]:
                return res
            index += 1
        res += " " 
        
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
