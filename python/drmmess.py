#!/usr/bin/env python
""" An attempt to solve drmmessages on Kattis """

import sys
from functools import lru_cache


# This seems ugly, but it'll work?
LETTER_TO_NUMBER = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5,
    "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11,
    "M": 12, "N": 13, "O": 14, "P": 15, "Q": 16, "R": 17,
    "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
    "Y": 24, "Z": 25
}

NUMBER_TO_LETTER = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F",
    6: "G", 7: "H", 8: "I", 9: "J", 10: "K", 11: "L",
    12: "M", 13: "N", 14: "O", 15: "P", 16: "Q", 17: "R",
    18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
    24: "Y", 25: "Z"
}


def divide(source):
    return (source[:int(len(source) / 2)], source[int(len(source) / 2):])


@lru_cache()
def rotate(source):
    rotation_value = 0
    for letter in source:
        rotation_value += LETTER_TO_NUMBER[letter]

    output_string = ""
    for letter in source:
        output_string += rotate_letter(letter, rotation_value)


    return output_string


@lru_cache()
def rotate_letter(letter, value):
    letter_number = LETTER_TO_NUMBER[letter]
    letter_number += value
    while letter_number > 25:
        letter_number = letter_number - 26
    return NUMBER_TO_LETTER[letter_number]


def merge(first, second):
    output_string = ""
    for i in range(len(first)):
        output_string += rotate_letter(first[i], LETTER_TO_NUMBER[second[i]])
    return output_string


def main():
    source = sys.stdin.read().rstrip()
    first_half, second_half = divide(source)
    first_half = rotate(first_half)
    second_half = rotate(second_half)
    result = merge(first_half, second_half)
    print(result)


if __name__ == "__main__":
    main()
