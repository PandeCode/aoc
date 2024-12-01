#!/bin/env python3

from pprint import pprint as p
from typing import Literal, final
from regex import finditer

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

MAXES = {
    "blue": 14,
    "green": 13,
    "red": 12,
}


def solve(_s: str):
    s = _s.split("\n")
    len_s = len(s)

    i = 0
    symbols_locations: list[set[int]] = []
    while i < len_s:
        symbols = finditer(r"[^\.\d]", s[i])
        symbols_locations.append(set([location.start() for location in symbols]))
        i += 1

    i = 0
    sum = 0
    while i < len_s:
        nums = finditer(r"\d+", s[i])

        for num in nums:
            start = num.start()
            end = num.end()
            range_start_end = set(range(start, end))

            curr_line = symbols_locations[i]
            next_line = symbols_locations[i + 1] if i != (len_s - 1) else set()
            prev_line = symbols_locations[i - 1] if i != 0 else set()

            if (
                end in curr_line
                or start - 1 in curr_line
                or end in next_line
                or start - 1 in next_line
                or end in prev_line
                or start - 1 in prev_line
                or range_start_end & prev_line
                or range_start_end & next_line
            ):
                sum += int(num.captures()[0])

        i += 1

    return sum


assert solve(example) == 4361

with open("./input.txt", "r") as f:
    challenge = f.read()

print(solve(challenge))
