#!/bin/python3

import math
import os
import random
import re
import sys


'''
fsqoiaidfaukvngpsugszsnseskicpejjvytviya
ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget
output:42

fcrxzwscanmligyxyvym
jxwtrhvujlmrpdoqbisbwhmgpmeoke
output:30
'''

if __name__ == '__main__':
    a = list("fcrxzwscanmligyxyvym")
    b = list("jxwtrhvujlmrpdoqbisbwhmgpmeoke")
    m = {}
    for i in a:
        if i not in m.keys():
            m[i] = 0
        if i in b:
            x = a.count(i)
            y = b.count(i)
            m[i] = max(x,y)-min(x,y)
        else:
            m[i] += 1

    for i in b:
        if i not in m.keys():
            m[i] = 0
        if i in a:
            x = a.count(i)
            y = b.count(i)
            m[i] = max(x,y)-min(x,y)
        else:
            m[i] += 1
    x = 0
    for k, v in m.items():
        x+=v
    print(x)

