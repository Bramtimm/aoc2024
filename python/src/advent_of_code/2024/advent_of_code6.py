import copy

from advent_of_code.utils import Matrix

class PositionMatrix(Matrix):

   
    def __init__(self, nrow, ncol):
        super().__init__(nrow, ncol, data=None)


    @property
    def starting_position(self):
        for col in range(0, self.ncol):
            for row in range(0, self.nrow):
                if self.data[row][col] == "^":
                    return row, col, "up"
                

    def set_deepcopy(self):
        self.deep_copy = copy.deepcopy(self.data)


    def move_position(self):
        row_index, col_index, direction = self.starting_position

        # also include starting position
        self.deep_copy[row_index][col_index] = 'X'
        
        while direction != "end":

            if direction == "up":
                row_index, col_index, direction = self.move_up(row_index, col_index, direction)
            elif direction == "right":
                row_index, col_index, direction = self.move_right(row_index, col_index, direction)
            elif direction == "down":
                row_index, col_index, direction = self.move_down(row_index, col_index, direction)
            elif direction == "left":
                row_index, col_index, direction = self.move_left(row_index, col_index, direction)
          
        
    def move_up(self, row_index, col_index, direction):
        try:
            step = self.data[row_index-1][col_index] 
            if  step == "." or step == "^":
                row_index = row_index-1
                self.deep_copy[row_index][col_index] = "X"
                direction = "up"
            elif step == "#":
                direction = "right"
        except IndexError:
            direction = "end"
        return row_index, col_index, direction
        
    def move_right(self, row_index, col_index, direction):
        try:
            step = self.data[row_index][col_index+1] 
            if  step == "." or step == "^":
                col_index = col_index+1
                self.deep_copy[row_index][col_index] = "X"
                direction = "right"
            elif step == "#":
                direction = "down"
        except IndexError:
            direction = "end"
        return row_index, col_index, direction
        
    def move_down(self, row_index, col_index, direction):
        try:
            step = self.data[row_index+1][col_index] 
            if  step == "." or step == "^":
                row_index = row_index+1
                self.deep_copy[row_index][col_index] = "X"
                direction = "down"
            elif step == "#":
                direction = "left"
        except IndexError:
            direction = "end"
        return row_index, col_index, direction
        
    def move_left(self, row_index, col_index, direction):
        try:
            step = self.data[row_index][col_index-1] 
            if  step == "." or step == "^":
                col_index = col_index-1
                self.deep_copy[row_index][col_index] = "X"
                direction = "left"
            elif step == "#":
                direction = "up"
        except IndexError:
            direction = "end"

        return row_index, col_index, direction
        
    def get_flatten(self):

        flatten_list = []
        for rows in self.deep_copy:
            flatten_list.extend(rows)
        
        return flatten_list
    
    def print_deepcopy(self):
        for rows in self.deep_copy:
            print(rows)


       
            


        



def advent_of_code6a(input_str: str) -> Matrix:

    puzzle_input = input_str.split()
    puzzle_input = [list(line) for line in puzzle_input]

    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])
    
    puzzle_matrix = PositionMatrix(nrow = nrows, ncol = ncols)

    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = puzzle_input[row][col]

    puzzle_matrix.set_deepcopy()
    puzzle_matrix.move_position()
    flatten_list = puzzle_matrix.get_flatten()
    
    return flatten_list.count("X")

def advent_of_code6b(input_str: str) -> int:

    puzzle_input = input_str.split()
    puzzle_input = [list(line) for line in puzzle_input]

    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])
    
    puzzle_matrix = PositionMatrix(nrow = nrows, ncol = ncols)

    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = puzzle_input[row][col]
    
    # TODO: safe index of moving up/down
    # TODO: place object on path
    # TODO: safe index of moving up/down
    # TODO: check whether second index is subset of first
    
    pass

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
    assert test_output == 41

    with open("../data/advent_of_code6/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code6a(puzzle_input)
    print(f"the answer to aoc6a is: {puzzle_output}")

    test_output = advent_of_code6b(test_input)
    assert test_output == 6