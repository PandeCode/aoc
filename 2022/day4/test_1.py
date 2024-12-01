#!/bin/env python3
from pprint import pprint

#  with open("./example_input", "r") as file:
with open("./input", "r") as file:
    text = file.read()

parsed_lines: list[tuple[range, range]] = []

for line in text.split("\n"):
    if line:
        part = line.split(",")

        mp0 = list(map(int, part[0].split("-")))
        mp1 = list(map(int, part[1].split("-")))

        mp0[1] += 1
        mp1[1] += 1

        obj = (
            range(*mp0),
            range(*mp1),
        )

        parsed_lines.append(obj)

full_pairs = 0
for p in parsed_lines:
    r0 = p[0]
    r1 = p[1]

    still_pair_1 = True
    for i in r1:
        if i not in r0:
            still_pair_1 = False
            break

    still_pair_0 = True
    for i in r0:
        if i not in r1:
            still_pair_0 = False
            break

    if still_pair_0 or still_pair_1:
        full_pairs += 1

print(full_pairs)
