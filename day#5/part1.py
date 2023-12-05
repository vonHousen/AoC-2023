import collections
import dataclasses
import re
from typing import Iterable

NUMBER_REGEX = re.compile(r"\d+")
ALMANAC_MAP_HEADER_REGEX = re.compile(r"(\w+-to-\w+) map:")
SINGLE_MAP_REGEX = re.compile(r"(\d+) (\d+) (\d+)")
ALMANAC_CATEGORIES = [
    "seed",
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
]


@dataclasses.dataclass
class AlmanacMap:
    """A sparse implementation of a dictionary with a range as a key."""
    delta_per_range: dict[tuple[int, int], int] = dataclasses.field(default_factory=dict)

    def update(self,
               source_category_id_since: int,
               destination_category_id_since: int,
               range_length: int) -> None:
        source_category_id_range = (source_category_id_since, source_category_id_since + range_length)
        self.delta_per_range[source_category_id_range] = destination_category_id_since - source_category_id_since

    def get(self, key: int) -> int:
        for (lower_boundary, upper_boundary), delta in self.delta_per_range.items():
            if lower_boundary <= key < upper_boundary:
                return key + delta
        else:
            return key


def get_lowest_location_number() -> None:
    with open("input.txt", "r") as f:
        almanac_lines = f.read().splitlines()

    almanac_seeds_line = almanac_lines[0]
    seeds = {int(number_match[0]) for number_match in NUMBER_REGEX.finditer(almanac_seeds_line)}

    almanac_map_names_ordered = [f"{category_from}-to-{category_to}"
                                 for category_from, category_to
                                 in zip(ALMANAC_CATEGORIES[:-1], ALMANAC_CATEGORIES[1:])]
    almanac_map_per_name = _parse_almanac(almanac_lines[1:])

    location_per_seed: dict[int, int] = {}
    for seed in seeds:
        key = seed
        for map_name in almanac_map_names_ordered:
            almanac_map = almanac_map_per_name[map_name]
            key = almanac_map.get(key)

        location_per_seed[seed] = key

    lowest_location_number = min(location_per_seed.values())
    print(f"Lowest location number is {lowest_location_number}")


def _parse_almanac(almanac_lines: Iterable[str]) -> dict[str, AlmanacMap]:
    current_almanac_map_name: str | None = None
    almanac_map_per_name: dict[str, AlmanacMap] = collections.defaultdict(AlmanacMap)

    for line in almanac_lines:
        if map_name_match := ALMANAC_MAP_HEADER_REGEX.search(line):
            current_almanac_map_name = map_name_match[1]
            continue

        single_map_match = SINGLE_MAP_REGEX.search(line)
        if not single_map_match:
            current_almanac_map_name = None
            continue

        assert current_almanac_map_name is not None
        destination_cat_id, source_cat_id, range_length = [int(number) for number in single_map_match.groups()]

        almanac_map_per_name[current_almanac_map_name].update(source_cat_id,
                                                              destination_cat_id,
                                                              range_length)

    return dict(almanac_map_per_name)


if __name__ == "__main__":
    get_lowest_location_number()
