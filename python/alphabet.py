#!/usr/bin/env python3
""" An attempt to solve the Alphabet problem on Kattis """

import sys

# This is a longest increasing sequence question.
# Strings can easily be expressed as integers via ord().  Algorithm and explanation here:
# http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence
# function lis_length( a )
#     n := a.length
#     q := new Array(n)
#     for k from 0 to n:
#         max := 0;
#         for j from 0 to k, if a[k] > a[j]:
#             if q[j] > max, then set max = q[j].
#         q[k] := max + 1;
#     max := 0
#     for i from 0 to n:
#         if q[i] > max, then set max = q[i].
#     return max;


def lis_length(a):
    n = len(a)
    q = [0] * n
    for k in range(0, n):
        maximum_length = 0
        for j in range(0, k):
            if ((a[k] > a[j]) and
                    q[j] > maximum_length):
                maximum_length = q[j]
        q[k] = maximum_length + 1
    maximum_length = 0
    for i in range(0, n):
        if q[i] > maximum_length:
            maximum_length = q[i]

    return maximum_length


def main():
    data = sys.stdin.readline().rstrip()
    # Can do this on the fly in lis_length.. or just do it in one step here
    line = [ord(letter) for letter in data]
    print(26 - lis_length(line))

if __name__ == "__main__":
    main()
