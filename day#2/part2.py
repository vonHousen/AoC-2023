from part1 import REGEX_PER_COLOUR


def sum_powers_of_min_cubes_sets() -> None:
    """
    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?
    """
    with open("input.txt", "r") as f:
        games_record = f.read().splitlines()

    powers_sum = sum(__calculate_power_of_minimum_set_of_cubes(single_game_record.split(":")[1])
                     for single_game_record
                     in games_record)

    print(f"Sum of the power is {powers_sum}.")


def __calculate_power_of_minimum_set_of_cubes(single_game_revealed_cubes: str) -> int:
    min_values_per_colour = {colour: 0 for colour in REGEX_PER_COLOUR}
    for game_round in single_game_revealed_cubes.split(";"):
        for colour, regex in REGEX_PER_COLOUR.items():
            matched_str = regex.search(game_round)
            if not matched_str:
                continue

            cubes_count = int(matched_str[1])
            min_values_per_colour[colour] = max(min_values_per_colour[colour], cubes_count)

    power_of_sets = 1
    for value in min_values_per_colour.values():
        power_of_sets *= value

    return power_of_sets


if __name__ == "__main__":
    sum_powers_of_min_cubes_sets()
