#!/usr/bin/env python

from itertools import *


def multiples():
    bottom = 1
    top = 1000

    return sum(list(x for x in range(bottom, top) if x % 3 == 0 or x % 5 == 0))


class Fibonacci_iter:

    def __init__(self):
        self.prev = 0
        self.result = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.result, self.prev = self.prev + self.result, self.result
        return self.result


def fibonacci_number(num):
    prev = 0
    result = 1
    for x in range(1, num):
        result, prev = prev + result, result
    return result


def fibonacci_gen():
    prev = 0
    result = 1

    while True:
        result, prev = prev + result, result
        yield result


def fibonacci():
    max_fib = 4000000

    # return sum(list(takewhile(
    #    lambda x: x < max_fib,
    #    filter(lambda x: x % 2 == 0, (fibonacci_number(x)
    #                                  for x in count(1))))))

    return sum(list(takewhile(
        lambda x: x < max_fib,
        (x for x in Fibonacci_iter() if x % 2 == 0))))

    # return sum(list(takewhile(
    #    lambda x: x < max_fib,
    #    (x for x in fibonacci_gen() if x % 2 == 0))))


def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[-1::-1]


def palindrome():
    # Python, однако (+1).
    max_count = 1000
    return max(x * y for x in range(100, max_count)
               for y in range(x, max_count) if is_palindrome(x * y))


def gen_ints():
    i = 0
    while True:
        yield i
        i += 1

print(multiples())
print(fibonacci())
print(palindrome())
