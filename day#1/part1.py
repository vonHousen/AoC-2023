from typing import Callable


def deobfuscate_calibration_document(deobfuscation_func: Callable[[str], int]) -> None:
    """
    The newly-improved calibration document consists of lines of text; each line originally contained a specific
    calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining
    the first digit and the last digit (in that order) to form a single two-digit number.

    Args:
        deobfuscation_func: Function that perform deobfuscation process on a single line.
    """
    with open("input_part1.txt", "r") as f:
        calibration_document_lines = f.read().splitlines()

    sum_of_all_calibration_values = sum(deobfuscation_func(line) for line in calibration_document_lines)

    print(f"Sum of all calibration values: {sum_of_all_calibration_values}.")


def deobfuscate_single_line(line: str) -> int:
    """
    Deobfuscate single line of calibration document.

    Args:
        line: Single line of calibration document

    Returns:
        Single calibration value.
    """
    first_digit = next(char for char in line if char.isdigit())
    last_digit = next(char for char in reversed(line) if char.isdigit())
    return int(first_digit + last_digit)


if __name__ == "__main__":
    deobfuscate_calibration_document(deobfuscate_single_line)
