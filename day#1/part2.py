from part1 import deobfuscate_calibration_document


natural_language_digits_map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}


def deobfuscate_single_line(line: str) -> int:
    """
    Deobfuscate single line of calibration document.

    Args:
        line: Single line of calibration document

    Returns:
        Single calibration value.
    """
    digits_per_position: dict[int, str] = {}
    for digit, natural_language_name in natural_language_digits_map.items():
        if (first_position := line.find(digit)) != -1:
            digits_per_position[first_position] = digit
        if (last_position := line.rfind(digit)) != -1:
            digits_per_position[last_position] = digit
        if (first_position := line.find(natural_language_name)) != -1:
            digits_per_position[first_position] = digit
        if (last_position := line.rfind(natural_language_name)) != -1:
            digits_per_position[last_position] = digit

    first_digit = next(
        digit for position, digit in sorted(digits_per_position.items(), key=lambda x: x[0])
    )
    last_digit = next(
        digit for position, digit in sorted(digits_per_position.items(), key=lambda x: x[0], reverse=True)
    )
    return int(first_digit + last_digit)


if __name__ == "__main__":
    deobfuscate_calibration_document(deobfuscate_single_line)
