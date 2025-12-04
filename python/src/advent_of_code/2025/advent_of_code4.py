from advent_of_code.utils import Matrix


def advent_of_code4(grid: list[int], can_be_removed: bool = False) -> int:
    accessible_toiletpaper = 0
    removable_toiletpaper = True

    # create matrix
    nrow = len(grid)
    ncol = nrow

    puzzle_matrix = Matrix(nrow, ncol, data=grid)

    while removable_toiletpaper:
        removable_toiletpaper = False
        for i in range(0, nrow):
            for j in range(0, ncol):
                
                if puzzle_matrix[i, j] == 0:
                    next
                if puzzle_matrix[i, j] == 1:
                    
                    row_slice = slice(max([i - 1, 0]), min(i + 2, nrow), 1)
                    col_slice = slice(max([j - 1, 0]), min(j + 2, ncol), 1)
                    # create adjacent matrix
                    adjacent_elements = puzzle_matrix[row_slice, col_slice]
                    if isinstance(adjacent_elements, Matrix):
                        adjacent_elements = adjacent_elements.flatten()
                    if sum(adjacent_elements) < 5:
                        accessible_toiletpaper += 1

                        if can_be_removed:
                            removable_toiletpaper = True
                            puzzle_matrix[i, j] = 0
                            
                        
    return accessible_toiletpaper


def advent_of_code4b() -> int:
    pass


if __name__ == "__main__":
    test_input = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    # make binary for speed
    test_input = [list(line) for line in test_input.split()]
    test_input = [
        [0 if ele == "." else 1 for ele in sub_list] for sub_list in test_input
    ]

    test_output = advent_of_code4(test_input)
    print(f"the test answer to aoc4a is: {test_output}")
    assert test_output == 13

    with open(
        "/home/bramtimm/code-projects/rust-python/advent_of_code/data/2025/advent_of_code4/puzzle_input.txt",
        "r",
    ) as f:
        puzzle_input = f.readlines()
        puzzle_input = [
            [0 if ele == "." else 1 for ele in sub_list] for sub_list in puzzle_input
        ]

    puzzle_output = advent_of_code4(puzzle_input)
    print(f"the answer to aoc4a is: {puzzle_output}")

    test_output = advent_of_code4(test_input, True)
    print(f"the test answer to aoc4b is: {test_output}")
    assert test_output == 43

    puzzle_output = advent_of_code4(puzzle_input, True)
    print(f"the answer to aoc4b is: {puzzle_output}")
