#!/usr/bin/env python


def front_x(words):
    first_char = "x"
    s_x = list(filter(lambda x: x.startswith(first_char), words))
    s_notx = list(filter(lambda x: not x.startswith(first_char), words))

    # Не лучше ли sorted() ?
    s_x.sort()
    s_notx.sort()

    return s_x + s_notx


print(front_x(["mix", "xyz", "apple", "xanadu", "aardvark"]))
