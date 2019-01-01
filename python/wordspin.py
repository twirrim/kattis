#!/usr/bin/env python3
""" An attempt to solve the WordSpin problem on Kattis
Note, this seems to produce correct output, I just can't get it to do it fast enough.
Testing against two 10 million character strings gets lands in about 2.5 seconds, give or take.

I might be able to parallelise this, but I wonder about the overhead """

import sys
import logging

logging.basicConfig(level=logging.INFO)

def minDistance(word1, word2):
    if len(word1) != len(word2):
        raise Exception("Words must be of equal length")
    word_length = len(word1)
    direction = [0] * (word_length+1)
    distance = [0] * word_length

    # Find out steps between each individual letter
    logging.info("Calculating basic distances")
    for i in range(word_length):
        # ord returns an int, e.g. ord("a") = 97.
        # In this situation, we can rely on it to measure distance
        distance[i] = ord(word2[i]) - ord(word1[i])

        # Noting direction here saves on some more complex logic later on.
        # Putting this logic later made for much harder to read code,
        # at a miniscule trade off of better memory consumption
        if distance[i] > 0:
            # Going forwards
            direction[i] += 1
        if distance[i] < 0:
            # Going backwards
            direction[i] -= 1
            distance[i] = abs(distance[i])

    direction[word_length] = 0
    steps = 0
    logging.info("Working out the number of steps")
    for i in range(word_length):
        # If neighbours need to go in different directions
        # just count the steps
        if direction[i] != direction[i+1]:
            steps += distance[i]
        else:
            if distance[i] > distance[i+1]:
                steps += (distance[i] - distance[i+1])

    return steps

def main():
    word1, word2 = sys.stdin.readline().rstrip().split(" ")
    print(minDistance(word1, word2))


if __name__ == "__main__":
    main()
