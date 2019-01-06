#!/usr/bin/env python

""" An attempt to solve the Anagram Counting puzzle on Kattis. """

import sys
from math import factorial
from collections import Counter


for line in sys.stdin.readlines():
    line = line.rstrip()
    line_details = Counter(line)
    divisor = 1
    for key in line_details:
        if line_details[key] > 1:
            divisor = divisor * factorial(line_details[key])
    print(factorial(len(line)) // divisor)
