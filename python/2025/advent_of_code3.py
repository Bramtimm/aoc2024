from itertools import combinations


# naive solution
def advent_of_code3a(input: list[str], length_of_combinations: int) -> int:
    combos = []

    for i in input:
        sets = combinations(i, length_of_combinations)

        current_max = int("".join(next(sets)))

        for i in sets:
            if int("".join(i)) > current_max:
                current_max = int("".join(i))
            else:
                next

        combos.append(current_max)

    return sum(combos)


def advent_of_code3b(input: list[str], length_of_combinations: int) -> int:
    combos = []

    [combos.append(get_largest_substring(i, length_of_combinations)) for i in input]

    return sum(combos)


def get_largest_substring(input: list[int], length_of_combinations: int) -> int:

    if len(input) < length_of_combinations:
        return

    largest_substring = []
    prev_index=0
    for i in reversed(range(0, length_of_combinations)):
        largest = max(input[prev_index:(len(input)-i)])
        prev_index=input.index(largest, prev_index)+1
        largest_substring.append(largest)

    return int("".join(largest_substring))


if __name__ == "__main__":
    test_input = """987654321111111
811111111111119
234234234234278
818181911112111"""

    test_input = test_input.split()
    test_input = [list(line) for line in test_input]

    test_output = advent_of_code3a(test_input, 2)
    print(f"the test answer to aoc3a is: {test_output}")
    assert test_output == 357

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code3/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.readlines()
        puzzle_input = [list(line.strip()) for line in puzzle_input]

    puzzle_output = advent_of_code3a(puzzle_input, 2)
    print(f"the answer to aoc3a is: {puzzle_output}")

    test_output = advent_of_code3b(test_input, 12)
    print(f"the test answer to aoc3b is: {test_output}")
    assert test_output == 3121910778619

    puzzle_output = advent_of_code3b(puzzle_input, 12)
    print(f"the answer to aoc3b is: {puzzle_output}")
