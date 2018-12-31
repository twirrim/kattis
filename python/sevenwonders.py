#!/usr/bin/env python
""" An Attempt to solve the Seven Wonders problem on Kattis """
import sys

hand = sys.stdin.read().rstrip()

result_dict = {"T": 0, "C": 0, "G": 0}

for card in hand:
    result_dict[card] += 1

# number of complete sets is equal to the minimum number of any one card
# just hard coding this would probably be quicker!
sets = -1
total_score = 0

for card, count in result_dict.items():
    total_score += pow(count, 2)
    if sets == -1:
        sets = count
    elif count < sets:
        sets = count

total_score += (sets * 7)
print(total_score)
