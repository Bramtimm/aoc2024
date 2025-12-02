import re


def advent_of_code2a(input: list[list[int]]) -> int:
    invalid_ids = []

    for id_range in input:
        ## find all ids
        ids = find_all_ids(id_range)
        ## regular expression
        pattern = re.compile(r"(.+?)\1")

        [
            invalid_ids.append(id)
            for id in ids
            if re.fullmatch(pattern, id) is not None
        ]

    return sum([int(id) for id in set(invalid_ids)])


def advent_of_code2b(input: list[list[int]]):
    
    invalid_ids = []

    for id_range in input:
        ## find all ids
        ids = find_all_ids(id_range)
        ## regular expression
        pattern = re.compile(r"(.+?)\1+")

        [
            invalid_ids.append(id)
            for id in ids
            if re.fullmatch(pattern, id) is not None
        ]

    return sum([int(id) for id in set(invalid_ids)])


def find_all_ids(id_range: list[int]) -> list[int]:
    start = int(id_range[0])
    end = int(id_range[1])

    id_range = list(range(start, end + 1))

    id_range = [str(id_code) for id_code in id_range]

    return id_range


# probably faster to use suffix tree with dp? --> will try later :)


if __name__ == "__main__":
    test_input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
    test_input = test_input.split(",")
    test_input = [subrange.split("-") for subrange in test_input]

    test_output = advent_of_code2a(test_input)
    print(f"the test answer to aoc2a is: {test_output}")
    assert test_output == 1227775554

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code2/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_input = puzzle_input.split(",")
        puzzle_input = [subrange.split("-") for subrange in puzzle_input]

    puzzle_output = advent_of_code2a(puzzle_input)
    print(f"the answer to aoc2a is: {puzzle_output}")

    test_output = advent_of_code2b(test_input)
    print(f"the test answer to aoc2b is: {test_output}")
    assert test_output == 4174379265

    puzzle_output = advent_of_code2b(puzzle_input)
    print(f"the answer to aoc2b is: {puzzle_output}")
