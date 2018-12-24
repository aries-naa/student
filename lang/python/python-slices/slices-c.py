#!/usr/bin/env python


def shift(s):
    words = s.split(" ")
    return " ".join(words[-1:] + words[:-1])


print(shift("a b c dd eee ffff"))
