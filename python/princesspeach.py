#!/usr/bin/env python3
""" Solving the Princess Peach puzzle on Kattis"""

import sys

data = sys.stdin.readline().rstrip()

n, y = data.split(" ")

obstacles = set(range(0, int(n)))
found = set()

for i in range(int(y)):
    entry = int(sys.stdin.readline().rstrip())
    found.add(entry)

for obstacle in sorted(obstacles-found):
    print("{}".format(obstacle))

print("Mario got {} of the dangerous obstacles.".format(len(found)))
