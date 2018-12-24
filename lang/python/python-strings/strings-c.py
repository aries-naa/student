#!/usr/bin/env python


def fix_start(s):
    first_char = s[0]
    tail = s[1:].replace(first_char, "*")

    return "{}{}".format(first_char, tail)


print(fix_start("babble"))
