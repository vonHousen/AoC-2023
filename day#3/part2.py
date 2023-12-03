import re
from math import prod

from part1 import _get_all_part_numbers


def sum_gear_ratios() -> None:
    """
    Sum all the gear ratios in the engine schematic.

    A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying
    those two numbers together.
    """
    with open("input.txt", "r") as f:
        engine_schematic = f.read().splitlines()

    gear_ratios = [prod(part_number.value for part_number in matched_symbol_adjacent_numbers)
                   for matched_symbol_adjacent_numbers in _get_all_part_numbers(engine_schematic, re.compile(r"[\*]"))
                   if len(matched_symbol_adjacent_numbers) == 2]
    gear_ratios_sum = sum(gear_ratios)

    print(f"The sum of all of the gear ratios: {gear_ratios_sum}.")


if __name__ == "__main__":
    sum_gear_ratios()
