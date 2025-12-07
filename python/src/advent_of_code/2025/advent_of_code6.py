import re
import math
from collections import deque

from advent_of_code.utils import Matrix


def advent_of_code6a(sums: list[int], operators=list[str]):
    sum_matrix = Matrix(len(sums), len(sums), sums)
    result_sum = 0
    for i in range(0, len(operators)):
        if operators[i] == "+":
            result_sum += sum(sum_matrix[:, i])
        elif operators[i] == "*":
            result_sum += math.prod(sum_matrix[:, i])

    return result_sum


# def advent_of_code6b(sums: list[str], operators=list[str]):
#     sum_matrix = Matrix(len(sums), len(sums), sums)
#     result_sum = 0

#     for i in range(0, len(operators)):
#         if operators[i] == "+":
#             result_sum += sum(read_cephalopod_math(sum_matrix[:, i]))
#         elif operators[i] == "*":
#             result_sum += math.prod(read_cephalopod_math(sum_matrix[:, i]))

#     return result_sum


# def read_cephalopod_math(inp_list: list[str]) -> list[int]:
#     cephalopod_list = [[] for _ in range(len(inp_list.data))]

#     for elements in inp_list:
#         elements = list(elements)

#         for no, element in enumerate(reversed(elements)):
#             no = len(inp_list.data) - no - 1
#             cephalopod_list[no].append(element)

#     return list(map(int, cephalopod_list))


if __name__ == "__main__":
    test_input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """

    # make binary for speed
    test_input = [line for line in test_input.split("\n")]
    test_operators = re.split(r"\s+", test_input[-1].strip())
    test_sums = [
        list(map(int, re.split(r"\s+", lines.strip()))) for lines in test_input[:-1]
    ]

    # test_sums_b = [line.split() for line in test_input[-1]]

    test_output = advent_of_code6a(sums=test_sums, operators=test_operators)
    print(f"the test answer to aoc6a is: {test_output}")
    assert test_output == 4277556

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code6/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_input = [line for line in puzzle_input.split("\n")]
        operators = re.split(r"\s+", puzzle_input[-1].strip())
        sums = [
            list(map(int, re.split(r"\s+", lines.strip())))
            for lines in puzzle_input[:-1]
        ]

        # sums_b = [re.split(r"\s{3}", lines) for lines in puzzle_input[:-1]]
        # sums_b = [re.split(r"\s{1}", sums_b_item) for sums_b_item in sums_b]

    puzzle_output = advent_of_code6a(sums, operators)
    print(f"the answer to aoc6a is: {puzzle_output}")

    # test_output = advent_of_code6b(test_sums_b, test_operators)
    # print(f"the test answer to aoc6b is: {test_output}")
    # assert test_output == 3263827

    # puzzle_output = advent_of_code6b(sums_b, operators)
    # print(f"the answer to aoc6b is: {puzzle_output}")
