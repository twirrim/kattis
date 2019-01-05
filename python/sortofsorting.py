#!/usr/bin/env python

""" An attempt to solve Sort Of Sorting on Kattis """

import sys


def is_int(entry):
    try:
        int(entry)
        return True
    except ValueError:
        return False


def main():
    start = True
    while True:
        line = sys.stdin.readline().rstrip()
        if is_int(line):
            if line == "0":
                break
            if start == True:
                start = False
            else:
                print()
            data = []
            for i in range(int(line)):
                data.append(sys.stdin.readline().rstrip())
            for entry in sorted(data, key=lambda student: student[:2]):
                print(entry)

if __name__ == "__main__":
    main()


