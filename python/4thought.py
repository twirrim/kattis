#!/usr/bin/env python3

# An attempt to solve 4thought problem on Kattis
#
# Yes, this is brute force, because I started thinking that might be interesting
# to do, and there's only 64 of them.
# With a max of 1000 integers, that's only 64,000 checks

import sys
import itertools
import re
from string import Template

# Note the //, that forces integer division
OPERATORS = ["+", "-", "*", "//"]
EXPRESSION = Template("4 $first 4 $second 4 $third 4")
CLEANUP_RE = re.compile(r"//")

possibilities = [perm for perm in itertools.product(OPERATORS, repeat=3)]

ignore = sys.stdin.readline()

test_cases = sys.stdin.readlines()

for test_case in test_cases:
    test_case = int(test_case.rstrip())
    output = "no solution"
    for possibility in possibilities:
        test_string = EXPRESSION.substitute(first=possibility[0],
                                            second=possibility[1],
                                            third=possibility[2])
        if eval(test_string) == test_case:
            output = "{} = {}".format(test_string, test_case)
            output = CLEANUP_RE.sub('/', output)
            break
    print(output)
