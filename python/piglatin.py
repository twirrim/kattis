#!/usr/bin/env python3

vowels = set(["a", "e", "i", "o", "u", "y"])


def gimme_the_answer(source):
    output = []
    for word in source.rstrip().split():
        output.append(pig_latin(word))
    print(' '.join(output))

def pig_latin(word):
    index = 0
    for letter in word:
        if letter in vowels:
            if index == 0:
                return word+"yay"
            break
        index += 1
    return word[index:] + word[:index] + "ay"


for line in open(0).readlines():
    gimme_the_answer(line)
