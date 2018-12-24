#!/usr/bin/env python


def even(s):
    return " ".join(s.split(" ")[1::2])


print(even("a b c d ee fff"))
