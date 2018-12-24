#!/usr/bin/env python


def donuts(count):
    return "Количество пончиков: {}".format(
        "много" if count >= 10 else str(count))


print(donuts(5))
print(donuts(10))
print(donuts(23))
