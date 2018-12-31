#!/usr/bin/env python3
""" Solving the Atori problem on Kattis """

# I'm not happy with this, but I think it meets requirements
# There are too many edge cases going on here, it feels like.

import sys

data = sys.stdin.read().strip()

authors = data.split("-")

result = ""
for name in authors:
    result = result+name[0]

print(result)
