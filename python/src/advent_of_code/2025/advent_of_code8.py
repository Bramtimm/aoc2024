from collections import defaultdict
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
                global_min = min_val

        prev_val = global_min

        connection_list.append((min_row, min_col))

    clusters = find_all_clusters(connection_list)

    size = sorted((len(cluster) for cluster in clusters), reverse=True)

    return math.prod(size[0:3])


def euclidian_distance(pos_1: list[int], pos_2: list[int]):
    dis = [(dim_1 - dim_2) ** 2 for dim_1, dim_2 in zip(pos_1, pos_2)]

    return math.sqrt(sum(dis))


def find_all_clusters(edge_list: list[tuple[int]]):
    graph = defaultdict(set)
    clusters = []

    for u, v in edge_list:
        graph[u].add(v)
        graph[v].add(u)

    def dfs(node, component):
        visited.add(node)
        component.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, component)

    all_nodes = set()
    visited = set()

    for u, v in edge_list:
        all_nodes.add(u)
        all_nodes.add(v)

    for node in all_nodes:
        if node not in visited:
            component = set()
            dfs(node, component)
            clusters.append(component)

    return clusters


def advent_of_code8b(grid_input: list[int]):
    dis_data = [
        euclidian_distance(pos_1, pos_2) for pos_1 in grid_input for pos_2 in grid_input
    ]
    max_value = max(dis_data)
    dis_mat = Matrix(len(grid_input), len(grid_input), dis_data)

    all_visited = 0
    prev_val = 0
    edge_list = []

    while all_visited < len(grid_input):
        prev_min_value = max_value
        for row in range(0, dis_mat.nrow):
            min_val = min(x for x in dis_mat[row] if x > prev_val)

            if min_val < prev_min_value and min_val > prev_val:
                min_row = row
                min_col = dis_mat[row].index(min_val)
                prev_min_value = min_val
                global_min = min_val

        prev_val = global_min

        edge_list.append((min_row, min_col))

        all_visited = len(set(tuple(x for pair in edge_list for x in pair)))

    left, right = edge_list[-1]

    return grid_input[left][0] * grid_input[right][0]


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

    test_grid = test_input.splitlines()
    test_grid = [list(map(int, line.split(","))) for line in test_grid]
    test_output = advent_of_code8a(grid_input=test_grid, num_connections=10)
    print(f"the test answer to aoc8a is: {test_output}")

    assert test_output == 40

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code8/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_grid = puzzle_input.splitlines()
        puzzle_grid = [list(map(int, line.split(","))) for line in puzzle_grid]

    puzzle_output = advent_of_code8a(puzzle_grid, num_connections=1000)
    print(f"the answer to aoc8a is: {puzzle_output}")

    test_output = advent_of_code8b(test_grid)
    print(f"the test answer to aoc8b is: {test_output}")
    assert test_output == 25272

    puzzle_output = advent_of_code8b(puzzle_grid)
    print(f"the answer to aoc8b is: {puzzle_output}")
