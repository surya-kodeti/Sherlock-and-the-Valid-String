#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    c = Counter(s)
    v = list(c.values())
    v = list(set(v))
    if len(v)==1:
        return "YES"
    else:
        l = list(s)
        C=0
        for i in c:
            temp = l
            temp.remove(i)
            T = Counter(temp)
            vT = set(T.values())
            temp.append(i)
            if len(vT)==1:
                C=-1
                break
    if C==-1:
        return "YES"
    else:
        return "NO"
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
