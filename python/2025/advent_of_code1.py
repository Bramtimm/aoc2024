def advent_of_code1a(puzzle_input: list[str]) -> int:
    # read to list and convert to numbers
    code_list = [
        int(item.removeprefix("R"))
        if item.startswith("R")
        else -int(item.removeprefix("L"))
        for item in puzzle_input
    ]

    starting_point = 50
    times_pointing_zero = 0

    for code in code_list:
        # get remainder of 100 as full round
        if code > 0:
            code = code % 100
        else:
            code = code % -100

        if starting_point + code >= 0 and starting_point + code < 100:
            starting_point += code
        elif starting_point + code < 0:
            remainder = starting_point + code
            starting_point = 100 + remainder
        elif starting_point + code > 100:
            starting_point = starting_point + code - 100
        else:
            starting_point = 0

        if starting_point == 0:
            times_pointing_zero += 1

    return times_pointing_zero


def advent_of_code1b(puzzle_input: list[str]) -> int:
    code_list = [
        int(item.removeprefix("R"))
        if item.startswith("R")
        else -int(item.removeprefix("L"))
        for item in puzzle_input
    ]

    starting_point = 50
    times_across_zero = 0
    times_pointing_zero = 0

    for code in code_list:
        if code > 0:
            times_across_zero += code // 100
            code = code % 100
        elif code < 0:
            times_across_zero += code // -100
            code = code % -100

        if starting_point + code > 0 and starting_point + code < 100:
            starting_point += code
        elif starting_point + code == 0 or starting_point + code == 100:
            starting_point = 0
            times_pointing_zero += 1

        elif starting_point + code < 0 and starting_point != 0:
            remainder = starting_point + code
            starting_point = 100 + remainder
            times_across_zero += 1
        elif starting_point + code < 0 and starting_point == 0:
            remainder = starting_point + code
            starting_point = 100 + remainder

        elif starting_point + code > 100:
            starting_point = starting_point + code - 100
            times_across_zero += 1

    return times_across_zero + times_pointing_zero


if __name__ == "__main__":
    test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

    test_input = test_input.split("\n")

    test_output = advent_of_code1a(test_input)
    print(f"the test answer to aoc1a is: {test_output}")
    assert test_output == 3

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code1/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.readlines()

    puzzle_output = advent_of_code1a(puzzle_input)
    print(f"the answer to aoc1a is: {puzzle_output}")

    test_output = advent_of_code1b(test_input)
    print(f"the test answer to aoc1b is: {test_output}")
    assert test_output == 6

    puzzle_output = advent_of_code1b(puzzle_input)
    print(f"the answer to aoc1b is: {puzzle_output}")
