#!/usr/bin/env python


def not_bad(s):
    bad = "плох"
    start = s.find("не")
    finish = s.rfind(bad)

    if start != -1 and finish != -1 and finish > start:
        return "{}{}{}".format(
            s[:start], "хорош", s[finish + len(bad):])
    else:
        return s


print(not_bad("Этот ужин не так уж плох!"))
print(not_bad("Этот ужин не так уж!"))
print(not_bad("Этот ужин плох уж не совсем!"))
