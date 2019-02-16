#!/usr/bin/env python
""" An attempt to solve "A Different Problem" on Kattis """

import sys

def main():
    data = [line.rstrip() for line in sys.stdin.readlines()]
    for line in data:
        first, second = line.split(" ")
        print("{}".format(abs(int(first) - int(second))))

if __name__ == "__main__":
    main()
