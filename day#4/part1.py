import re

NUMBER_REGEX = re.compile(r"\d+")


def get_total_points_in_scratchcards() -> None:
    with open("input.txt", "r") as f:
        scratchcards_with_names = f.read().splitlines()

    total_points = sum(_get_number_of_points(scratchcard_with_name.split(":")[1])
                       for scratchcard_with_name in scratchcards_with_names)

    print(f"There are {total_points} points in total.")


def _get_selected_numbers_that_won(scratchcard: str) -> set[int]:
    """
    Get number of points gained on the single scratchcard.

    Single scratchcard has two lists of numbers separated by a vertical bar (|): a list of winning numbers
    and then a list of numbers you have. Figure out which of the numbers you have appeared in the list of winning
    numbers. The first match makes the card worth one point and each match after the first doubles the point value of
    that card.
    """
    winning_numbers_str, selected_numbers_raw = scratchcard.split("|")
    winning_numbers = {int(matched_number[0]) for matched_number in NUMBER_REGEX.finditer(winning_numbers_str)}
    selected_numbers = {int(matched_number[0]) for matched_number in NUMBER_REGEX.finditer(selected_numbers_raw)}
    return winning_numbers & selected_numbers


def _get_number_of_points(scratchcard: str) -> int:
    """
    Get number of points gained on the single scratchcard.

    Single scratchcard has two lists of numbers separated by a vertical bar (|): a list of winning numbers
    and then a list of numbers you have. Figure out which of the numbers you have appeared in the list of winning
    numbers. The first match makes the card worth one point and each match after the first doubles the point value of
    that card.
    """
    if selected_winning_numbers := _get_selected_numbers_that_won(scratchcard):
        return int(2 ** (len(selected_winning_numbers) - 1))
    else:
        return 0


if __name__ == "__main__":
    get_total_points_in_scratchcards()
