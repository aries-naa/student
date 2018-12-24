#!/usr/bin/env python


def match_ends(words):
    count = 0
    for element in words:
        if len(element) >= 2 and element[0] == element[-1]:
            count += 1
    return count


print(match_ends(["", "12", "123", "1234"]))
print(match_ends(["", "12", "123", "1234", "11"]))
print(match_ends(["", "12", "123", "1234", "11", "-12345-"]))
