from advent_of_code.utils import Matrix

def advent_of_code9a(coordinates: list[int]):

    areas = []
    for left_coordinate in coordinates:
        for right_coordinate in coordinates:

            length = abs(left_coordinate[0] - right_coordinate[0])+1
            width = abs(left_coordinate[1] - right_coordinate[1])+1
            areas.append(rectangle_area(width, length))

    return max(areas)
        


def rectangle_area(width: int, length: int):
    return width * length

if __name__ == "__main__":
    test_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

    test_grid = test_input.splitlines()
    test_grid = [list(map(int, line.split(","))) for line in test_grid]
    test_output = advent_of_code9a(coordinates=test_grid)
    print(f"the test answer to aoc9a is: {test_output}")

    assert test_output == 50

    with open(
        "/home/sagemaker-user/aoc2024/data/2025/advent_of_code9/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_grid = puzzle_input.splitlines()
        puzzle_grid = [list(map(int, line.split(","))) for line in puzzle_grid]

    puzzle_output = advent_of_code9a(puzzle_grid)
    print(f"the answer to aoc9a is: {puzzle_output}")

    test_output = advent_of_code9b(test_grid)
    print(f"the test answer to aoc9b is: {test_output}")
    assert test_output == 25272

    puzzle_output = advent_of_code9b(puzzle_grid)
    print(f"the answer to aoc9b is: {puzzle_output}")
