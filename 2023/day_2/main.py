#!/bin/env python3

from pprint import pprint as p
from typing import Literal, final

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

MAXES = {
    "blue": 14,
    "green": 13,
    "red": 12,
}

def solve(i: str):
    games = dict()
    for line in i.split("\n"):
        if line:
            l = [r.split(",") for r in line[line.find(":") +1:].split(";")]
            key_name = line[ 5: line.find(":") ]

            g = []
            for m in l:
                t: dict[str | Literal["blue", "red", "green"], int] = dict()
                for k in m:
                    s = k.strip().split(" ")
                    t[s[1]] = int(s[0])
                g.append(t)

            games[int(key_name)] = g

    index_sum = 0
    for id, game in games.items():
        shouldContinue = False

        for round in game:
            round["red"] = round.get("red") or 0
            round["green"] = round.get("green") or 0
            round["blue"] = round.get("blue") or 0

            if round["red"] > MAXES["red"] or round["blue"] > MAXES["blue"] or round["green"] > MAXES["green"]:
                id = 0

        index_sum += id

    return index_sum


assert solve(example) == 8

with open("./input.txt", "r") as f:
    challenge = f.read()

print(solve(challenge))
