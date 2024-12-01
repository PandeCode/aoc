#!/bin/env python3
from pprint import pprint

#  with open("./example_input", "r") as file:
with open("./input", "r") as file:
	text = file.read()


lines = text.split("\n")

moves: list[tuple[int, int, int]] = []
collect_data = True
index = 0

for i, line in enumerate(lines[0 : len(lines) - 1]):
	if not line:
		collect_data = False
		index = i
	elif collect_data:
		pass
	else:
		raw_moves = line.split()
		moves.append((int(raw_moves[1]), int(raw_moves[3]), int(raw_moves[5])))

data: dict[int, list[str]] = {int(i): [] for i in lines[index - 1].split()}

for data_line in lines[0 : index - 1]:
	i = 0
	blocks: list[str] = []

	len_data_line = len(data_line)
	while i < len_data_line:
		blocks.append(data_line[i : i + 4])
		i += 4

	for i, block in enumerate(blocks):
		block = block.replace("[", "").replace("]", "").replace(" ", "")
		if block != "":
			data[i + 1].append(block)

for move in moves:
	number = move[0] 
	from_ = move[1]
	to = move[2]

	to_move : list[str] = []
	for _ in range(number):
		to_move = [ *to_move, data[from_].pop(0)]

	data[to] = [*to_move, *data[to]]


for v in data.values():
	print(v[0],end="")

