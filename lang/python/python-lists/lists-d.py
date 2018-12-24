#!/usr/bin/env python


def remove_adjacent(nums):
    result = []

    for element in nums:
        if len(result) == 0 or element != result[-1]:
            result.append(element)
    return result


print(remove_adjacent([]))
print(remove_adjacent([1, 2, 2, 3, 4, 4]))
print(remove_adjacent([1, 1, 2, 2, 2, 3, 2, 2]))
