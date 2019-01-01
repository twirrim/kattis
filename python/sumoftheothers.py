#!/usr/bin/env python3

""" This is an attempt to solve the Sum Of The Others problem on Kattis """

import sys
import logging


def main():
    for entry in sys.stdin.readlines():
        data = entry.rstrip(" ").split(" ")
        logging.info("Input: {}".format(data))
        to_evaluate = '+'.join(data)
        logging.info("Evaluate: {}".format(to_evaluate))
        result = eval(to_evaluate)
        logging.info("Result: {}".format(result))
        for number in data:
            number = int(number)
            if result - number == number:
                print(number)
                break



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO)
    main()
