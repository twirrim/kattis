#!/usr/bin/env python
""" An attempt to solve the Alphabet Spam problem on kattis """

import sys
import re
import logging

logging.basicConfig(level=logging.INFO)

data = sys.stdin.readline().rstrip()

length = len(data)
number_of_lower = len(re.findall(r"[a-z]", data))
number_of_upper = len(re.findall(r"[A-Z]", data))
number_of_whitespaces = len(re.findall(r"_", data))
number_of_symbols = len(re.findall(r"[^a-zA-Z_]", data))

percent_per_character = 1.0/length

logging.info("length: {}\tlower: {}\tupper: {}\twhitespace: {}\tsymbols: {}".format(
    length, number_of_lower, number_of_upper, number_of_whitespaces,
    number_of_symbols))

print(format(percent_per_character * number_of_whitespaces, '.15g'))
print(format(percent_per_character * number_of_lower, '.15g'))
print(format(percent_per_character * number_of_upper, '.15g'))
print(format(percent_per_character * number_of_symbols, '.15g'))
