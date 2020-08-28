#!/usr/bin/python


def parse(p):
    chars = []  # where all the characters go
    calc = []  # where all the maths goes
    result = []  # where my results go
    operator = "+-"
    # round 0: read from left to right
    # strip everything down to characters
    for c in p.replace(" ", ""):
        chars.append(c)

    i = 0
    maxI = len(chars)
    while i < maxI:
        # round 1: check if number
        if chars[i].isnumeric():
            # if 2 is the only thing on the paper, return
            if len(chars) == 1:
                result.append(chars[i])
            # if not, continue calculations
            else:
                calc.append(chars[i])
        else:
            result.append("")
        i += 1

    return chars, result


string = parse("2    +   ")
print(string)
