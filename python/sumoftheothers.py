#!/usr/bin/env python3

""" This is an attempt to solve the Sum Of The Others problem on Kattis """

import sys


def main():
    for entry in sys.stdin.readlines():
        data = entry.rstrip(" ").split(" ")
        result = eval('+'.join(data))
        for number in data:
            number = int(number)
            if result - number == number:
                print(number)
                break

if __name__ == "__main__":
    main()
