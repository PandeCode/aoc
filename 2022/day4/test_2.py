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

intersections = 0
for p in parsed_lines:
	r0 = p[0]
	r1 = p[1]

	found = False
	for i in r1:
		if i in r0:
			found = True
			break

	if found:
		intersections += 1
		continue

	for i in r0:
		if i in r1:
			found = True
			break

	if found:
		intersections += 1

print(intersections)
