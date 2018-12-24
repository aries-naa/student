#!/usr/bin/env python


def inside(s):
    words = s.split(" ")
    middle = int(len(words) / 2)
    return " ".join(words[1:middle] + [words[0], words[-1]] + words[middle:-1])


print(inside("a b c d e f"))
