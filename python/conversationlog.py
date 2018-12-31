#!/usr/bin/env python3
""" An attempt to solve the Conversation Log problem on Kattis """

import sys
import logging

logging.basicConfig(level=logging.INFO)

ignored = sys.stdin.readline()

all_unique_words = set()
words = dict()
wordcount = dict()

for line in sys.stdin:
    data = line.rstrip().split(" ")
    if data[0] not in words:
        words[data[0]] = set()
    for index in range(1, len(data)):
        try:
            wordcount[data[index]] += 1
        except KeyError:
            wordcount[data[index]] = 1
        finally:
            words[data[0]].add(data[index])
            all_unique_words.add(data[index])

logging.info("words: {}\nwordcount: {}\nall_unique_words: {}".format(
    words, wordcount, all_unique_words))

for person in words:
    all_unique_words.intersection_update(words[person])
logging.info("all_unique_words:{}".format(all_unique_words))

if all_unique_words:
    results = [[i, wordcount[i]] for i in all_unique_words]
    sorted_results = sorted(results, key=lambda x: (-x[1], x[0]))
    for result in sorted_results:
        print(result[0])
else:
    print("ALL CLEAR")
