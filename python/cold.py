#!/usr/bin/env python3

""" An attempt to solve the Cold-puter Science problem on Kattis """

import sys


ignore = sys.stdin.readline()

temps = sys.stdin.readline().rstrip().split(" ")

total = 0
for temp in temps:
    if temp.startswith("-"):
        total += 1

print(total)
