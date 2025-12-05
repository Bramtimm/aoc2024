from itertools import batched
from dataclasses import dataclass


@dataclass
class MemoryBlock:
    block_type: int
    files: list[int]
    space_length: int

    TYPE_FILE = 1
    TYPE_SPACE = 0


def advent_of_code9a(input_string: str) -> int:
    pairs = list(batched(input_string, n=2))

    # files = [pair[0] for pair in pairs]
    # files_with_id = {str(i+1): value for i, value in enumerate(files)}
    # free_space = [pair[1] for pair in pairs if len(pair)==2]

    for pair in pairs:
        pass


def _check_sum(output) -> int:
    0

    pass


if __name__ == "__main__":
    test_input = """2333133121414131402"""

    test_output = advent_of_code9a(test_input)
    print(f"Test output: {test_output}")
    assert test_output == 1928

    with open("../advent_of_code9/input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code9a(puzzle_input)
    print(f"Puzzle output: {puzzle_output}")
