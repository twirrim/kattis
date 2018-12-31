#!/usr/bin/env python3
""" An attemtp to solve qaly problem on Kattis """

import sys

# We don't really care about the first line
number_of_periods_of_quality = sys.stdin.readline()

# Read the rest in, which we do care about
periods_of_life = sys.stdin.readlines()

# Start as a float
qaly = 0.0
for period in periods_of_life:
    q, y = period.strip().split(" ")
    qaly = qaly + (float(q) * float(y))

print("{:.3f}".format(qaly))
