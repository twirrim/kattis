#!/usr/bin/env python3
""" An attemtp to solve "Sum Kind of Problem" on Kattis """

import sys

# We don't really care about the first line
sys.stdin.readline()

# Read the rest in, which we do care about
datasets = sys.stdin.readlines()

for dataset in datasets:
    k, n = dataset.split(" ")
    k = int(k)
    n = int(n)
    s1 = int((n * (n + 1))/ 2)
    s3 = s1 * 2
    s2 = s3 - n

    print("{} {} {} {}".format(k, s1, s2, s3))
