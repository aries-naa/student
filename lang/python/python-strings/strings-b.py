#!/usr/bin/env python


def both_ends(s):
    if len(s) >= 2:
        return "{}{}".format(s[:2], s[-2:])
    else:
        return ""


print(both_ends("1"))
print(both_ends("12"))
print(both_ends("spring"))
