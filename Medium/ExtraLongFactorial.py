# https://www.hackerrank.com/challenges/extra-long-factorials/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'extraLongFactorials' function below.
#
# The function accepts INTEGER n as parameter.
#

def extraLongFactorials(n):
    # Write your code here
    fact = 1
    while(n>0):
      fact *= n
      n -= 1
      
    print(fact)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)
