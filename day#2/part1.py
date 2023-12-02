import re

GAME_ID_REGEX = re.compile("Game (\d+)")
REGEX_PER_COLOUR = {
    "r": re.compile("(\d+) red"),
    "g": re.compile("(\d+) green"),
    "b": re.compile("(\d+) blue"),
}
LIMIT_PER_COLOUR = {
    "r": 12,
    "g": 13,
    "b": 14,
}


def sum_ids_of_possible_games() -> None:
    """
    Sum IDs of possible games.

    You play several games and record the information from each game (your puzzle input). Each game is listed with its
    ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were
    revealed from the bag (like 3 red, 5 green, 4 blue).
    """
    with open("input.txt", "r") as f:
        games_record = f.read().splitlines()

    possible_games_ids_sum = sum(int(GAME_ID_REGEX.search(single_game_record)[1])
                                 for single_game_record
                                 in games_record
                                 if __is_game_possible(single_game_record.split(":")[1]))

    print(f"Sum of IDs for possible games: {possible_games_ids_sum}.")


def __is_game_possible(single_game_revealed_cubes: str) -> bool:
    for game_round in single_game_revealed_cubes.split(";"):
        for colour, regex in REGEX_PER_COLOUR.items():
            matched_str = regex.search(game_round)
            if not matched_str:
                continue

            cubes_count = int(matched_str[1])
            if cubes_count > LIMIT_PER_COLOUR[colour]:
                return False

    return True


if __name__ == "__main__":
    sum_ids_of_possible_games()
