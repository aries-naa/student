#!/usr/bin/env python


def diff():
    # Python, однако (+1).
    sqr_count = 101

    # sum_of_sqr = sum([x**2 for x in range(1, sqr_count)])
    # sqr_of_sum = sum([x for x in range(1, sqr_count)])**2

    sum_of_sqr = sum(map(lambda x: x**2, range(1, sqr_count)))
    sqr_of_sum = sum(map(lambda x: x, range(1, sqr_count)))**2

    return sum_of_sqr - sqr_of_sum


def max_five():

    numerals_list = "12345678902"
    numerals_count = 5

    def mult(num_str):
        num_list = list(int(x) for x in num_str)
        result = num_list[0]

        for num in num_list[1:]:
            result *= num

        return result

    mult_list = list(mult(numerals_list[x:x + numerals_count])
                     for x in range(len(numerals_list) -
                                    numerals_count + 1))
    return max(mult_list)


def summm():
    return sum(list(int(x) for x in str(2**1000)))


def fac(num):
    result = 1
    for x in range(1, num):
        result *= x
    return result


def factorial():
    return sum(list(int(x) for x in str(fac(100))))


print(diff())
print(max_five())
print(summm())
print(factorial())
