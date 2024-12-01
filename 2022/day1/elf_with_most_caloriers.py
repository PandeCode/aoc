#!/bin/env python3
from pprint import pprint

print = pprint

file = open("./input", "r")
input_text = file.read()
file.close()

largest_sum  = 0
for items in input_text.split("\n\n"):
	s = sum(map(int, items.split()))
	largest_sum = largest_sum if largest_sum > s else s

print(largest_sum)
