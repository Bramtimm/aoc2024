def advent_of_code9(coordinates: list[int], check_validity: bool = False):
    areas = []
    validity = []
    for left_coordinate in coordinates:
        for right_coordinate in coordinates:
            length = abs(left_coordinate[0] - right_coordinate[0]) + 1
            width = abs(left_coordinate[1] - right_coordinate[1]) + 1
            areas.append(rectangle_area(width, length))

            if check_validity:
                valid = is_valid(left_coordinate, right_coordinate, coordinates)
                validity.append(valid)

    if check_validity:
        areas = [area for area, keep in zip(areas, validity) if keep]

    return max(areas)


def is_valid(left_coordinate, right_coordinate, coordinates):
    horiz_validity = 0
    vert_validity = 0

    for coordinate in coordinates:
        if left_coordinate[0] == right_coordinate[0] or left_coordinate[1]==right_coordinate[1]:
            continue

        if left_coordinate[0] > right_coordinate[0]:
            vert_range = range(left_coordinate[0], right_coordinate[0]-1, -1)
        else:
            vert_range = range(left_coordinate[0], right_coordinate[0]+1)
        if left_coordinate[1] > right_coordinate[1]:
            horiz_range = range(left_coordinate[1], right_coordinate[1]-1, -1)
        else:
            horiz_range = range(left_coordinate[1], right_coordinate[1]+1)

        if coordinate[0] in vert_range:
            vert_validity += 1
        if coordinate[1] in horiz_range:
            horiz_validity += 1

    if vert_validity > 2 or horiz_validity > 2:
        return False

    return True


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
    test_output = advent_of_code9(coordinates=test_grid)
    print(f"the test answer to aoc9a is: {test_output}")

    assert test_output == 50

    with open(
        "data/2025/advent_of_code9/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_grid = puzzle_input.splitlines()
        puzzle_grid = [list(map(int, line.split(","))) for line in puzzle_grid]

    puzzle_output = advent_of_code9(puzzle_grid)
    print(f"the answer to aoc9a is: {puzzle_output}")

    test_output = advent_of_code9(test_grid, check_validity=True)
    print(f"the test answer to aoc9b is: {test_output}")
    assert test_output == 24

    puzzle_output = advent_of_code9(puzzle_grid, check_validity=True)
    print(f"the answer to aoc9b is: {puzzle_output}")
