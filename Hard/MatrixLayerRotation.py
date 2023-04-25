# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'matrixRotation' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY matrix
#  2. INTEGER r
#

def matrixRotation(matrix, r):
    # Write your code here
    mat = []
    for i in range(min(m,n) // 2):
        temp = []
        for j in range(i, n-1-i):
            temp.append(matrix[i][j])
        for j in range(i, m-1-i):
            temp.append(matrix[j][n-1-i])
        for j in range(n-1-i, i, -1):
            temp.append(matrix[m-1-i][j])
        for j in range(m-1-i, i, -1):
            temp.append(matrix[j][i])
        mat.append(temp)
  
    for i in range(min(m, n) // 2):
        row = mat[i]
        rot_index = r % len(row)
        mat[i] = mat[i][rot_index:] + mat[i][:rot_index]

    
    for i in range(min(m,n) // 2):
        layer = mat[i]
        index = 0
        for j in range(i, n-1-i):
            matrix[i][j] = layer[index]
            index = (index+1) % len(layer)
        for j in range(i, m-1-i):
            matrix[j][n-1-i] =layer[index]
            index = (index+1) % len(layer)
        for j in range(n-1-i, i, -1):
            matrix[m-1-i][j] = layer[index]
            index = (index+1) % len(layer)
        for j in range(m-1-i, i, -1):
            matrix[j][i] = layer[index]
            index = (index+1) % len(layer)
          
    for row in matrix:
      print(*row)
          
      




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    r = int(first_multiple_input[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
