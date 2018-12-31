#!/usr/bin/env python3
""" An attempt to solve the Last Factorial Digit """

import sys

# This is totally wrong, but given N maxes out at 10, and anything after 5 the last digit is 0,
# this is likely cheaper and faster
result_dict = {1: 1,
               2: 2,
               3: 6,
               4: 4}

dont_care = sys.stdin.readline()

for line in sys.stdin.readlines():
    number = int(line.rstrip())
    if number >= 5:
        print(0)
    else:
        print(result_dict[number])
