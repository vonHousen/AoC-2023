from collections import Counter
import re
from typing import Iterable

from part1 import _get_selected_numbers_that_won


CARD_NAME_REGEX = re.compile(r"Card\s+(\d+)")


def get_number_of_won_scratchcards() -> None:
    with open("input.txt", "r") as f:
        scratchcards_with_names = f.read().splitlines()

    scratchcard_per_id = {__get_scratchcard_id(scratchcard_with_name): scratchcard_with_name.split(":")[1]
                          for scratchcard_with_name in scratchcards_with_names}

    # separate counting and evaluation of scratchcards, assuming that evaluation is computationally heavier
    winning_scratchcard_id_map = {scratchcard_id: __get_won_scratchcard_ids(scratchcard_id, scratchcard)
                                  for scratchcard_id, scratchcard in scratchcard_per_id.items()}

    # at first count originals
    original_and_copies_counter = Counter(scratchcard_per_id.keys())

    # then count copies
    __sum_won_cards(card_ids_to_sum=winning_scratchcard_id_map.keys(),
                    winning_scratchcard_id_map=winning_scratchcard_id_map,
                    counter=original_and_copies_counter)

    print(f"There are {original_and_copies_counter.total()} scratchcards in total.")


def __sum_won_cards(card_ids_to_sum: Iterable[int],
                    winning_scratchcard_id_map: dict[int, list[int]],
                    counter: Counter) -> None:
    # Recurrence may not be the fastest implementation, but it is more readable than a loop I think
    for card_id in card_ids_to_sum:
        won_card_ids = winning_scratchcard_id_map[card_id]
        counter.update(won_card_ids)
        __sum_won_cards(won_card_ids, winning_scratchcard_id_map, counter)


def __get_scratchcard_id(scratchcard_with_name: str) -> int:
    try:
        return int(CARD_NAME_REGEX.search(scratchcard_with_name)[1])
    except TypeError:
        raise NotImplementedError


def __get_won_scratchcard_ids(scratchcard_id: int, scratchcard: str) -> list[int]:
    if numbers := _get_selected_numbers_that_won(scratchcard):
        won_scratchcards_count = len(numbers)
        return list(range(scratchcard_id + 1, scratchcard_id + won_scratchcards_count + 1))
    else:
        return []


if __name__ == "__main__":
    get_number_of_won_scratchcards()
