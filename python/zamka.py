#!/usr/bin/env python3
""" Solving the Zamka problem on Kattis """

import sys
import logging

logging.basicConfig(level=logging.INFO)

l, d, x = sys.stdin.read().strip().split('\n')
l = int(l)
d = int(d)
x = int(x)
logging.info("l:{}\td:{}\tx:{}".format(l, d, x))

for n in range(l, d+1):
    logging.info("Starting n: {}.  Target x: {}".format(n, x))
    result = 0
    for number in str(n):
        result = result + int(number)
        if result > x:
            break
    if result == x:
        print(n)
        break

for m in range(d, l-1, -1):
    logging.info("Starting m: {}.  Target x: {}".format(m, x))
    result = 0
    for number in str(m):
        result = result + int(number)
        if result > x:
            break
    if result == x:
        print(m)
        break
