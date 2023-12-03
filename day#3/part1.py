import dataclasses
import re
from typing import Iterable


VECTORS_TO_CHECK_ADJACENCY = [
    (0, -1),  # left
    (-1, -1),  # upper-left
    (-1, 0),  # up
    (-1, 1),  # upper-right
    (0, 1),  # right
    (1, 1),  # lower-right
    (1, 0),  # down
    (1, -1),  # lower-left
]


@dataclasses.dataclass(frozen=True)
class PartNumber:
    value: int
    number_id: int

    def __repr__(self) -> str:
        return str(self.value)


def sum_all_part_numbers() -> None:
    """
    Sum all the part numbers in the engine schematic.

    The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of
    numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally,
    is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
    """
    with open("input.txt", "r") as f:
        engine_schematic = f.read().splitlines()

    part_numbers_sum = sum(__get_all_part_numbers(engine_schematic))

    print(f"The sum of all of the part numbers in the engine schematic: {part_numbers_sum}.")


def __get_all_part_numbers(engine_schematic: list[str]) -> list[int]:
    numbers_occurrence_2d_map = __get_numbers_occurrence_2d_map(engine_schematic)

    symbol_regex = re.compile(r"[^\d\.]")
    adjacent_numbers: list[PartNumber] = []
    for row_idx, line in enumerate(engine_schematic):
        for matched_symbol in symbol_regex.finditer(line):
            col_idx = matched_symbol.start()
            last_part_number_id = None
            for row_idx_addend, col_idx_addend in VECTORS_TO_CHECK_ADJACENCY:
                found_number = numbers_occurrence_2d_map.get((row_idx + row_idx_addend, col_idx + col_idx_addend))
                if found_number is None:
                    continue
                if found_number.number_id == last_part_number_id:
                    continue

                adjacent_numbers.append(found_number)
                last_part_number_id = found_number.number_id

    return [part_number.value for part_number in adjacent_numbers]


def __get_numbers_occurrence_2d_map(engine_schematic: Iterable[str]) -> dict[tuple[int, int], PartNumber]:
    number_regex = re.compile(r"\d+")
    part_number_id = 0
    numbers_occurrence_2d_map: dict[tuple[int, int], PartNumber] = {}

    for row_idx, line in enumerate(engine_schematic):
        for matched_symbol in number_regex.finditer(line):
            number = int(matched_symbol[0])
            potential_part_number = PartNumber(value=number, number_id=part_number_id)

            start_idx, end_idx = matched_symbol.start(), matched_symbol.end()
            for col_idx in range(start_idx, end_idx):
                numbers_occurrence_2d_map[row_idx, col_idx] = potential_part_number

            part_number_id += 1

    return numbers_occurrence_2d_map


if __name__ == "__main__":
    sum_all_part_numbers()
