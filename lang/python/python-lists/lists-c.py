#!/usr/bin/env python


def sort_last(lists):
    lists.sort(key=lambda x: x[-1])
    return lists


print(sort_last([[2, 2], [1, 3], [3, 4, 5], [1, 7]]))
