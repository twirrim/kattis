#!/usr/bin/env python3
""" Solve the Faktor problem on kattis """

import sys

# Given rounding up, just deduct 1 from the target case,
# Multiply the first by the modified second, and then add 1 to the result

data = sys.stdin.read().strip().split(" ")
data[0] = float(data[0])
data[1] = float(data[1]) - 1
result = data[0] * data[1]
print(int(result + 1))
