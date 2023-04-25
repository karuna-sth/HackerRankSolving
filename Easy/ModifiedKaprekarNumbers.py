# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    count = 0
    for i in range(p,q+1):
      digit = 0
      num = i
      result = 0
      
      result_list = ""
      square = i*i
      while num>0:
        digit +=1
        num = num//10;
      div = int('1'+('0'*digit))
      while square>0:
        result += square % div
        square = square // div
      if result == i:
        print(i, end=' ')
        count += 1
    
    if count == 0:
        print("INVALID RANGE")
        
        
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
