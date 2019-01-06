#!/usr/bin/env python3
""" An Attempt to solve the Backspace problem on Kattis """

import sys


data = list(sys.stdin.readline().rstrip())

output = []

index = 0
while True:
    try:
        if data[index] != "<":
            output.append(data[index])
        else:
            output.pop(len(output) - 1)
        index += 1
    except IndexError:
        # Got to the end
        break
    
print(''.join(output))
