def advent_of_code4a(test_input) -> int:
    return 0


class Matrix:

    def __init__(self, nrow: int, ncol: int, fill: str = ""):
        self.nrow = nrow
        self.ncol = ncol
        self.data = [[fill for _ in range(ncol)] for _ in range(nrow)]

    def __getitem__(self, index):
        row_index, col_index = index
        return self.data[row_index][col_index]
    
    def __setitem__(self, index, value):
        row_index, col_index = index
        self.data[row_index][col_index] = value

    # TODO: extract diagonal

    # TODO: make slicing possible

    # TODO: iterate over matrix

    



if __name__ == "__main__":
    
    test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

    test_output = advent_of_code4a(test_input)
    # assert test_output == 18

    with open("../data/advent_of_code4/puzzle_input.txt", "r") as f:
        puzzle_input = [line.split() for line in f if line.strip()]
        puzzle_input = [list(line[0]) for line in puzzle_input]
    
    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])

    puzzle_matrix = Matrix(nrow = nrows, ncol = ncols)

    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = puzzle_input[row][col]

    print(puzzle_matrix.data)