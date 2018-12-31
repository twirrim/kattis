#!/usr/bin/env python

import sys

def sum_to_n(n, size, limit=None):
    """Produce all lists of `size` positive integers in decreasing order
    that add up to `n`."""
    if size == 1:
        yield [n]
        return
    if limit is None:
        limit = n
    start = (n + size - 1) // size
    stop = min(limit, n - size + 1) + 1
    for i in range(start, stop):
        for tail in sum_to_n(n - i, size - 1, i):
            yield [i] + tail


# This seems ugly, but it'll work?
NUMBER_TO_LETTER = {
    1: "a", 2: "b", 3: "c", 4: "d", 5: "e",
    6: "f", 7: "g", 8: "h", 9: "i", 10: "j",
    11: "k", 12: "l", 13: "m", 14: "n", 15: "o",
    16: "p", 17: "q", 18: "r", 19: "s", 20: "t",
    21: "u", 22: "v", 23: "w", 24: "x", 25: "y",
    26: "z"
}

def main():
    length, score = sys.stdin.read().rstrip().split(" ")
    length = int(length)
    score = int(score)

    try:
        for combo in sum_to_n(score, length, limit=26):
            letters = [NUMBER_TO_LETTER[number] for number in combo]
            word = ''.join(letters)
            print(word)
            sys.exit(0)
    except Exception:
        pass
    print("impossible")


if __name__ == "__main__":
    main()
