from advent_of_code4 import Matrix

class PositionMatrix(Matrix):

    def __init__(self):
        pass

    # def get_position(self):

    #     position == "^"
    #     if position == "^":
    #         direction = "up"
    #     elif position == ">":
    #         direction = "right"
    #     elif position == "<":
    #         direction = "left"
    #     elif position == "V":
    #         direction == "down"

    



def advent_of_code6a(input_str: str) -> Matrix:

    puzzle_input = input_str.split()
    puzzle_input = [list(line) for line in puzzle_input]

    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])
    
    puzzle_matrix = Matrix(nrow = nrows, ncol = ncols)

    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = puzzle_input[row][col]

    
    return puzzle_matrix.data

if __name__ == "__main__":

    test_input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    test_output = advent_of_code6a(test_input)
    print(test_output)
    assert test_output == 41