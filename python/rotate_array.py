import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    i = len(a)
    ret = {}
    
    for x in range(i):
        print("a[%d]=%d  -> a[%d]=%d" % (x, a[x], (x-d+i)%i, a[x]))
        ret[ (x-d+i)%i ] = a[x]
    return ret
if __name__ == '__main__':

    a = [1, 2, 3, 4, 5]
    d = 4
    result = rotLeft(a, d)
    out = ""
    for x in range(len(a)):
        out += str(result[x]) + " "
    print(out)