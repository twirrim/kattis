#!/usr/bin/env python3
""" An attempt to solve the WordSpin problem on Kattis """

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
    for i in range(word_length):
        # ord returns an int, e.g. ord("a") = 97.
        # In this situation, we can rely on it to measure distance
        distance[i] = ord(word2[i]) - ord(word1[i])

        # Noting direction here saves on some more complex logic later on.
        # Putting this logic later made for much harder to read code,
        # at a miniscule trade off of better memory consumption
        if distance[i] > 0:
            logging.info("Going forwards")
            direction[i] += 1
        if distance[i] < 0:
            logging.info("Going backwards")
            direction[i] -= 1
            distance[i] = abs(distance[i])

    direction[word_length] = 0
    logging.info("distance:{}\tdirection:{}".format(distance, direction))
    steps = 0
    for i in range(word_length):
        # If neighbours need to go in different directions
        # just count the steps
        if direction[i] != direction[i+1]:
            logging.info("Neighbours don't need to go the same way! Adding {}".format(
                abs(distance[i])))
            steps += distance[i]
        else:
            logging.info("Neighbours match")
            if distance[i] > distance[i+1]:
                logging.info("{} > {}.  Adding first".format(distance[i], distance[i+1]))
                steps += (distance[i] - distance[i+1])
            else:
                logging.info("{} < {}.  Skipping".format(distance[i], distance[i+1]))

    return steps

def main():
    word1, word2 = sys.stdin.readline().rstrip().split(" ")
    print(minDistance(word1, word2))


if __name__ == "__main__":
    main()
