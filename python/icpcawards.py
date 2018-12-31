#!/usr/bin/env python3

import sys


# Don't care about the first record
null = sys.stdin.readline()

colleges_seen = set()

winners = 0

for line in sys.stdin.readlines():
    if winners == 12:
        break
    college, team = line.rstrip().split(' ')
    if college in colleges_seen:
        continue
    else:
        colleges_seen.add(college)
        print(college, team)
        winners += 1
