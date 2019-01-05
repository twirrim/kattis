#!/usr/bin/env python
""" An attempt to solve the Another Candies problem on Kattis """

import sys


def confirm_its_possible(test_case):
    children = int(test_case[0])
    number_of_candies = 0
    for i in range(1, children + 1):
        number_of_candies += int(test_case[i])
    if number_of_candies % children == 0:
        print("YES")
    else:
        print("NO")


def main():
    # We don't care about the first line
    sys.stdin.readline()
    # We do care about the rest
    data = sys.stdin.readlines()
    test_case = []
    for line in data:
        line = line.rstrip()
        if not line:
            if test_case:
                confirm_its_possible(test_case)
                test_case = []
        else:
            test_case.append(line)
    confirm_its_possible(test_case)


if __name__ == "__main__":
    main()
