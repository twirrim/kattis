#!/usr/bin/env python3

""" An attempt to solve Trik on Kattis """

import sys

"""
Ball starts in left most position.
[1, 0, 0]
A = positions 0 and 1 switch
B = positions 1 and 2 switch
C = positions 0 and 2 switch
"""


data = sys.stdin.read().rstrip()

board = [1, 0, 0]

for move in data:
    new = [0, 0, 0]
    if move == "A":
        new[0] = board[1]
        new[1] = board[0]
        new[2] = board[2]
    elif move == "B":
        new[0] = board[0]
        new[1] = board[2]
        new[2] = board[1]
    elif move == "C":
        new[0] = board[2]
        new[1] = board[1]
        new[2] = board[0]
    board = new

for i in range(len(board)):
    if board[i] == 1:
        print(i+1)
