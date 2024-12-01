#!/bin/env python3
from pprint import pprint

print = pprint

file = open("./input", "r")
input_text = file.read()
file.close()

sums : list[int] = []
for items in input_text.split("\n\n"):
	sums.append( sum(map(int, items.split())))
sums.sort(reverse=True);
print(sum(sums[:3]))

