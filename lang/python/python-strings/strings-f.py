#!/usr/bin/env python


def front_back(a, b):

    def split_string(s):
        middle = len(s) // 2 + len(s) % 2
        return (s[:middle], s[middle:])

    (a1, a2) = split_string(a)
    (b1, b2) = split_string(b)
    return "{}+{}+{}+{}".format(a1, b1, a2, b2)


print(front_back("12345", "abcd"))
