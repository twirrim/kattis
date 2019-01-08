#!/usr/bin/env python3
""" An Attempt to solve the Backspace problem on Kattis """

import sys


def process_line(line):
    output = []

    for index in range(len(line)):
        if line[index] == "<":
            output.pop()
        else:
            output.append(line[index])
    return ''.join(output)


if __name__ == "__main__":
    data = list(sys.stdin.readline().rstrip())

    print(process_line(data))
