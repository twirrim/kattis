#!/usr/bin/env python3

""" An Attempt to solve the Tarifa problem on Kattis """

import sys

megabyte_limit = int(sys.stdin.readline().rstrip())

ignored = sys.stdin.readline()

remaining = 0

for month in sys.stdin.readlines():
    remaining += (megabyte_limit - int(month.rstrip()))

print(remaining + megabyte_limit)
