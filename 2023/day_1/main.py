#!/bin/env python3

from string import ascii_lowercase

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def solve(i: str):
    sum = 0
    for line in i.split("\n"):
        if line:
            num = ""
            for c in line:
                if c not in ascii_lowercase:
                    num += c
            sum += int(num[0] + num[-1])

    return sum


assert solve(example) == 142

with open("./input.txt", "r") as f:
	challenge = f.read()

print(solve(challenge))
