import re

from part1 import __get_numbers_occurrence_2d_map, VECTORS_TO_CHECK_ADJACENCY, PartNumber


def sum_gear_ratios() -> None:
    """
    Sum all the gear ratios in the engine schematic.

    A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying
    those two numbers together.
    """
    with open("input.txt", "r") as f:
        engine_schematic = f.read().splitlines()

    gear_ratios_sum = sum(__get_all_gear_ratios(engine_schematic))

    print(f"The sum of all of the gear ratios: {gear_ratios_sum}.")


def __get_all_gear_ratios(engine_schematic: list[str]) -> list[int]:
    numbers_occurrence_2d_map = __get_numbers_occurrence_2d_map(engine_schematic)

    symbol_regex = re.compile(r"\*")
    gear_ratios: list[int] = []
    for row_idx, line in enumerate(engine_schematic):
        for matched_symbol in symbol_regex.finditer(line):
            col_idx = matched_symbol.start()
            last_part_number_id = None
            adjacent_numbers: list[PartNumber] = []
            for row_idx_addend, col_idx_addend in VECTORS_TO_CHECK_ADJACENCY:
                found_number = numbers_occurrence_2d_map.get((row_idx + row_idx_addend, col_idx + col_idx_addend))
                if found_number is None:
                    continue
                if found_number.number_id == last_part_number_id:
                    continue

                adjacent_numbers.append(found_number)
                last_part_number_id = found_number.number_id

            if len(adjacent_numbers) == 2:
                gear_ratios.append(adjacent_numbers[0].value * adjacent_numbers[1].value)

    return gear_ratios


if __name__ == "__main__":
    sum_gear_ratios()
