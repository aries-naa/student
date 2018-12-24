#!/usr/bin/env python


def mix_up(a, b):
    # А чё, нет функции или метода заменяющего символ в строке ?
    return "{}{}{} {}{}{}".format(
        a[:1], b[1], a[2:], b[:1], a[1], b[2:])


print(mix_up("mix", "pod"))
print(mix_up("dog", "dinner"))
