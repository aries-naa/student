#!/usr/bin/env python


def palindrome(d):
    return d == d[::-1]


print(palindrome("123456789"))
print(palindrome("123321"))
print(palindrome("123 v 321"))
