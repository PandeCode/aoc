#!/bin/env python3

from functools import reduce
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

    gear_locations: list[list[int]] = [
        [location.start() for location in finditer(r"\*", line)] for line in s
    ]
    number_locations: list[list[tuple[int, range]]] = [
        [
            (int(location.captures()[0]), range(location.start(), location.end(0)))
            for location in finditer(r"\d+", line)
        ]
        for line in s
    ]

    i = 0
    sum = 0
    while i < len_s:
        gears = gear_locations[i]
        prod_list: dict[int, list[int]] = dict()

        for num in number_locations[i]:
            for k, g in enumerate(gears):
                if num[1].start - 1 == g or num[1].stop == g:
                    prod_list[k] = [*(prod_list.get(k) or []), num[0]]

        if i != len_s - 1:
            for k, g in enumerate(gears):
                for num in number_locations[i + 1]:
                    if num[1].start - 1 == g or num[1].stop == g or g in num[1]:
                        prod_list[k] = [*(prod_list.get(k) or []), num[0]]

        if i != 0:
            for k, g in enumerate(gears):
                for num in number_locations[i - 1]:
                    if num[1].start - 1 == g or num[1].stop == g or g in num[1]:
                        prod_list[k] = [*(prod_list.get(k) or []), num[0]]

        for prods in prod_list.values():
            if len(prods) > 1:
                sum += reduce(lambda a, x: x * a, prods)

        i += 1

    return sum


assert solve(example) == 467835

with open("./input.txt", "r") as f:
    challenge = f.read()

print(solve(challenge))
