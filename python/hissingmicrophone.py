#!/usr/bin/env python
""" An Attempt to solve the Hissing Microphone problem on Kattis """

# This one is really straightforward on python, via any number of mechanisms
import sys
import re

hiss_re = re.compile(r"ss")

if hiss_re.search(sys.stdin.read()):
    print("hiss")
else:
    print("no hiss")