#!/usr/bin/env python3
""" Solving for Carrots on Kattis """
import sys

# This is daft.  Just return the second number on the first line of input.

data = sys.stdin.readline().strip().split(" ")

print(data[1])
