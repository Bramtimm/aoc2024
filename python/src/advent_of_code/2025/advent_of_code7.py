from advent_of_code.utils import Matrix


def advent_of_code7a(grid_input: list[str]):
    grid_input = Matrix(len(grid_input), len(grid_input), grid_input)

    start_position = find_starting_position(grid_input)
    split = 0
    start_position, split, grid_input = move_beam_down(start_position, grid_input, split)

    return split


def find_starting_position(grid_input):
    for row in range(0, len(grid_input.data)):
        for col in range(0, len(grid_input[0])):
            if grid_input[row, col] == "S":
                return row, col


def move_beam_down(
    start_position: tuple[int],
    grid_input: Matrix,
    split: int,
) -> int:
    row, col = start_position
    
    if row+1 < len(grid_input.data):
        if grid_input[row + 1, col] == ".":
                start_position = (row + 1, col)
                grid_input[start_position] = "|"
                start_position, split, grid_input = move_beam_down(start_position, grid_input, split)
        elif grid_input[row + 1, col] == "^":
                start_position_1 = (row + 1, col - 1)
                start_position_2 = (row + 1, col + 1)
                split += 1
                grid_input[start_position_1] = "|"
                grid_input[start_position_2] = "|"
                start_position, split, grid_input = move_beam_down(start_position_1, grid_input, split)
                start_position, split, grid_input = move_beam_down(start_position_2, grid_input, split)
        elif grid_input[row + 1, col] == "|":
                return start_position, split, grid_input

    return start_position, split, grid_input

def advent_of_code7b(grid_input: list[str]) -> int:
    
    grid_input = Matrix(len(grid_input), len(grid_input), grid_input)

    start_position = find_starting_position(grid_input)
    timeline = 0
    start_position, timeline, grid_input = move_beam_down_timeline(start_position, grid_input, timeline)

    return timeline

def move_beam_down_timeline(
    start_position: tuple[int],
    grid_input: Matrix,
    timeline: int,
) -> int:
    row, col = start_position

    if row+1 < len(grid_input.data):
        if grid_input[row + 1, col] == ".":
                start_position = (row + 1, col)
                grid_input[start_position] = "|"
                start_position, timeline, grid_input = move_beam_down_timeline(start_position, grid_input, timeline)
        elif grid_input[row + 1, col] == "^":
                start_position_1 = (row + 1, col - 1)
                start_position_2 = (row + 1, col + 1)
                
                if start_position_1[1] < len(grid_input[0]) and start_position_1[1]>=0:
                     timeline += 1
                
                if start_position_2[1] < len(grid_input[0]) and start_position_2[1]>=0:
                     timeline += 1
                    
                grid_input[start_position_1] = "|"
                grid_input[start_position_2] = "|"
                start_position, timeline, grid_input = move_beam_down_timeline(start_position_1, grid_input, timeline)
                start_position, timeline, grid_input = move_beam_down_timeline(start_position_2, grid_input, timeline)
       
    return start_position, timeline, grid_input

if __name__ == "__main__":
    test_input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    # make binary for speed
    test_grid = test_input.splitlines()
    test_grid = [list(line) for line in test_grid]
    test_output = advent_of_code7a(grid_input=test_grid)
    print(f"the test answer to aoc7a is: {test_output}")

    assert test_output == 21

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code7/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.read()
        puzzle_grid = puzzle_input.splitlines()
        puzzle_grid = [list(line) for line in puzzle_grid]

    puzzle_output = advent_of_code7a(puzzle_grid)
    print(f"the answer to aoc7a is: {puzzle_output}")

    test_grid = test_input.splitlines()
    test_grid = [list(line) for line in test_grid]
    test_output = advent_of_code7b(test_grid)
    print(f"the test answer to aoc7b is: {test_output}")
    assert test_output == 40

    # puzzle_output = advent_of_code5b(id_ranges)
    # print(f"the answer to aoc5b is: {puzzle_output}")
