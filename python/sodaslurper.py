#!/usr/bin/env python3

import sys
import logging
from math import floor

logging.basicConfig(level=logging.INFO)

empty, found, need = sys.stdin.readline().rstrip().split(" ")
empty = int(empty)
found = int(found)
need = int(need)

drunk = 0
logging.info("Empty: {}\tFound: {}\tNeed: {}".format(empty, found, need))

while empty + found >= need:
    empty = empty + found
    found = 0
    drunk_this_round = floor(empty / need)
    empty = empty - (drunk_this_round * need)
    drunk += drunk_this_round
    empty += drunk_this_round
    logging.info("End of round: Empty: {}\tFound: {}\tNeed: {}".format(empty, found, need))

logging.info("Empty: {}\tFound: {}\tNeed: {}\tDrunk: {}".format(empty, found, need, drunk))
print(drunk)
