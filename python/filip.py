#!/usr/bin/env python3

""" An attempt to solve the filip problem on Kattis """

import sys

first, second = sys.stdin.readline().rstrip().split(' ')

def flip_and_convert_to_int(source):
    return int(source[::-1])

flipped_first = flip_and_convert_to_int(first)
flipped_second = flip_and_convert_to_int(second)

if flipped_first > flipped_second:
    print(flipped_first)
else:
    print(flipped_second)
