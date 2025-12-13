import math
from advent_of_code.utils import Matrix


def advent_of_code8a(grid_input: list[int], num_connections: int):
    dis_mat = [
        euclidian_distance(pos_1, pos_2) for pos_1 in grid_input for pos_2 in grid_input
    ]

    max_value = max(dis_mat)

    dis_mat = Matrix(len(grid_input), len(grid_input), dis_mat)

    connection_list = []

    prev_val = 0
    
    ## find minimum value after 0, connect boxes
    for connection in range(0, num_connections):
        prev_min_value = max_value
        for row in range(0, dis_mat.nrow):
            min_val = min(x for x in dis_mat[row] if x > prev_val)

            if min_val < prev_min_value and min_val > prev_val:
                min_row = row
                min_col = dis_mat[row].index(min_val)
                prev_min_value = min_val

        prev_val = min_val

        connection_list.append((min_row, min_col))

    

    return connection_list


def euclidian_distance(pos_1: list[int], pos_2: list[int]):
    dis = [(dim_1 - dim_2) ** 2 for dim_1, dim_2 in zip(pos_1, pos_2)]

    return math.sqrt(sum(dis))


if __name__ == "__main__":
    test_input = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""

    # make binary for speed
    test_grid = test_input.splitlines()
    test_grid = [list(map(int, line.split(","))) for line in test_grid]
    test_output = advent_of_code8a(grid_input=test_grid, num_connections=10)
    print(f"the test answer to aoc8a is: {test_output}")

    assert test_output == 21

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code7/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_grid = puzzle_input.splitlines()
        puzzle_grid = [list(line) for line in puzzle_grid]

    puzzle_output = advent_of_code8a(puzzle_grid)
    print(f"the answer to aoc8a is: {puzzle_output}")

    test_grid = test_input.splitlines()
    test_grid = [list(line) for line in test_grid]
    test_output = advent_of_code8b(test_grid)
    print(f"the test answer to aoc8b is: {test_output}")
    assert test_output == 40

    puzzle_grid = puzzle_input.splitlines()
    puzzle_grid = [list(line) for line in puzzle_grid]

    puzzle_output = advent_of_code8b(puzzle_grid)
    print(f"the answer to aoc8b is: {puzzle_output}")
