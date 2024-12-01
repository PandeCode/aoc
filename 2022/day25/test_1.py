#!/bin/env python3
from pprint import pprint

#  with open("./input", "r") as file
with open("./example_input", "r") as file:
    text = file.read()

map_snafu_decimal = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2,
}
map_decimal_snafu = {value: key for key, value in map_snafu_decimal.items()}

def decimal_to_snafu(decimal: int):
	closest = 0
	smallest_range = 0

	pwr = -1
	while 5**pwr < decimal:
		pwr += 1;

		new_range =  decimal - 5 ** pwr
		if new_range < smallest_range:
			smallest_range = abs(new_range)
			closest = pwr

	print(smallest_range)
	print(closest)



print(" SNAFU: Decimal")

print("1=-0-2:   1747", decimal_to_snafu(1747))

#  print(" 12111:    906", decimal_to_snafu(906))
#  print("  2=0=:    198", decimal_to_snafu(198))
#  print("    21:     11", decimal_to_snafu(11))
#  print("  2=01:    201", decimal_to_snafu(201))
#  print("   111:     31", decimal_to_snafu(31))
#  print(" 20012:   1257", decimal_to_snafu(1257))
#  print("   112:     32", decimal_to_snafu(32))
#  print(" 1=-1=:    353", decimal_to_snafu(353))
#  print("  1-12:    107", decimal_to_snafu(107))
#  print("    12:      7", decimal_to_snafu(7))
#  print("    1=:      3", decimal_to_snafu(3))
#  print("   122:     37", decimal_to_snafu(37))
