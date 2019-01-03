#!/usr/bin/env python3
""" An Attempt to solve the FBI Universal Control Numbers problem on Kattis
Passes 1, fails 2 """

import sys

trans = {'B': '8', 'G': 'C', 'I': '1', 'O': '0',
         'Q': '0', 'S': '5', 'U': 'V', 'Y': 'V', 'Z': '2'}

reference = "0123456789ACDEFHJKLMNPRTVWX"
normal = "0123456789ABCDEFGHIJKLMNOPQ"

def integer_to_base_27(number):
    expandeducn = list(number)
    normalucn = []
    for i, letter in enumerate(expandeducn):
        normalucn.append(normal[reference.index(letter)])

    return int(''.join(normalucn), 27)

def repair_ucn(ucn):
    ucn = list(ucn)
    for i, letter in enumerate(ucn):
        if letter in trans:
            ucn[i] = trans[letter]
    return ''.join(ucn)

def get_checkbit(ucn):
    ucn = list(ucn)

    # (2*D1 + 4*D2 + 5*D3 + 7*D4 + 8*D5 + 10*D6 + 11*D7 + 13*D8) mod 27
    checksum = (2*reference.index(ucn[1]) + 4*reference.index(ucn[2]) +
                5*reference.index(ucn[3]) + 7*reference.index(ucn[4]) +
                8*reference.index(ucn[5]) + 10*reference.index(ucn[6]) +
                11*reference.index(ucn[7]) + 13*reference.index(ucn[8])) % 27

    return checksum

def is_valid_ucn(ucn):
    if ucn == '' or len(ucn) != 9:
        return False
    ref = set(list(reference))
    for letter in ucn:
        if not letter in ref and not letter in trans:
            return False
    return True

def process_line(line):
    # Get the data
    try:
        testcase, ucn = line.rstrip().split(" ")
    except ValueError:
        print("{} Invalid".format(line.rstrip()))
        return

    if not is_valid_ucn(ucn):
        print("{} Invalid".format(testcase))
        return

    ucn = repair_ucn(ucn)
    checkbit = get_checkbit(ucn)
    checksum = integer_to_base_27(ucn[:8])

    if str(checksum)[-1:] == str(checkbit):
        # Number is good!
        print(testcase, checksum)
    else:
        print("{} Invalid".format(testcase))


def main():
    # Skip the first line
    sys.stdin.readline()
    # Loop through the test cases
    for line in sys.stdin.readlines():
        process_line(line)

if __name__ == "__main__":
    main()
