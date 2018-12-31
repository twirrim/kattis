#!/usr/bin/env python

import sys

mapping = {"A":0, "B":1, "C":2}

data = sys.stdin.readline().rstrip().split(" ")
order = sys.stdin.readline().rstrip()

# Casting to int
numbers = []
for number in data:
    numbers.append(int(number))

# Now we know that A = 0, B = 1, C = 2
numbers = sorted(numbers)

output = ""
for letter in order:
    output += "{} ".format(str(numbers[mapping[letter]]))
print(output.rstrip(" "))
