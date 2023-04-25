# https://www.hackerrank.com/challenges/time-conversion/problem

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
    s_list = s.split(":")
    if(s_list[-1][-2:] == 'PM'):
        s_list[0] = s_list[0] if s_list[0] == '12' else str(int(s_list[0])+12)
    else:
        s_list[0] = '00' if s_list[0]=='12' else s_list[0]
    return((":".join(s_list))[:-2])
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
