#!/usr/bin/env python


def reverse(s):
    return " ".join(s.split(" ")[::-1])


print(reverse("a b c dd eee"))
