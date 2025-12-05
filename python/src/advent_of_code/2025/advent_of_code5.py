def advent_of_code5a(ids: list[int], id_ranges: list[tuple[int]]) -> int:
    # sort id_ranges by first key
    id_ranges = sorted(id_ranges, key=lambda key: key[0])

    fresh_id_counter = 0
    for id in ids:
        for id_range in id_ranges:
            min_id, max_id = id_range
            if id >= min_id and id <= max_id:
                fresh_id_counter += 1
                break

    return fresh_id_counter


def advent_of_code5b(id_ranges: list[tuple[int]]) -> int:
    # sort id_ranges by first key
    id_ranges = sorted(id_ranges, key=lambda key: key[0])

    fresh_id_counter = 0
    count_id = 0

    for id_range in id_ranges:
        min_id, max_id = id_range
        if min_id > count_id and count_id < max_id:
            fresh_id_counter += max_id - min_id + 1
            count_id = max_id
        elif min_id <= count_id and count_id <= max_id:
            fresh_id_counter += max_id - count_id
            count_id = max_id

    return fresh_id_counter


if __name__ == "__main__":
    test_input = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

    # make binary for speed
    test_id_ranges = [line.split("-") for line in test_input.split("\n\n")[0].split()]
    test_id_ranges = [
        tuple(int(ele) for ele in id_range) for id_range in test_id_ranges
    ]
    test_ids = list(map(int, test_input.split("\n\n")[1].split()))

    test_output = advent_of_code5a(test_ids, test_id_ranges)
    print(f"the test answer to aoc5a is: {test_output}")
    # assert test_output == 3

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code5/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        id_ranges = [line.split("-") for line in puzzle_input.split("\n\n")[0].split()]
        id_ranges = [tuple(int(ele) for ele in id_range) for id_range in id_ranges]
        ids = list(map(int, puzzle_input.split("\n\n")[1].split()))

    puzzle_output = advent_of_code5a(ids, id_ranges)
    print(f"the answer to aoc5a is: {puzzle_output}")

    test_output = advent_of_code5b(test_id_ranges)
    print(f"the test answer to aoc5b is: {test_output}")
    assert test_output == 14

    puzzle_output = advent_of_code5b(id_ranges)
    print(f"the answer to aoc5b is: {puzzle_output}")
