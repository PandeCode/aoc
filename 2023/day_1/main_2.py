#!/bin/env python3

from string import ascii_lowercase

example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

num_str = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    *[str(i) for i in range(1, 10)],
]


def convert(s):
    if len(s) == 1:
        return int(s)
    return int(num_str.index(s)) + 1


def get_first_num(s: str):
    m: dict[int, str] = dict()
    for num in num_str:
        n = s.find(num)
        if n != -1:
            m[n] = num
    return m[min(m.keys())]


def get_last_num(s: str):
    m: dict[int, str] = dict()
    for num in num_str:
        n = s.rfind(num)
        if n != -1:
            m[n] = num
    return m[max(m.keys())]


def solve(i: str):
    sum = 0
    for line in i.split("\n"):
        if line:
            first = str(convert(get_first_num(line)))
            last = str(convert(get_last_num(line)))
            sum += int(first + last)

    return sum

assert solve(example) == 281

with open("./input_2.txt", "r") as f:
    challenge = f.read()

print(solve(challenge))
