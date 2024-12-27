from itertools import starmap, pairwise
from operator import sub

from utils import Matrix


def advent_of_code_10a(puzzle_input: str) -> int:

    puzzle_input = puzzle_input.split()
    puzzle_input = [list(line) for line in puzzle_input]
    
    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])

    puzzle_matrix = TopoMatrix(nrow = nrows, ncol = ncols)
    
    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = int(puzzle_input[row][col])

    puzzle_matrix.print_matrix()
    print(puzzle_matrix.trailhead_locations)
    print(puzzle_matrix.trailpeak_locations)
    # puzzle_matrix.slope_matrix()
    return 0

class TopoMatrix(Matrix):

    def __init__(self, nrow, ncol):
        super().__init__(nrow, ncol)
      

    @property
    def trailhead_locations(self) -> list[tuple]:
        starting_positions = []
        for row in range(0, self.nrow):
            for col in range(0, self.ncol):
                if self.data[row][col] == 0:
                    starting_positions.append((row, col))
        
        return starting_positions
    
    @property
    def trailpeak_locations(self) -> list[tuple]:
        peak_positions = []
        for row in range(0, self.nrow):
            for col in range(0, self.ncol):
                if self.data[row][col] == 9:
                    peak_positions.append((row, col))
        
        return peak_positions
    
    def traverse_topomatrix():
        pass
        #TODO

        

 
    # def slope_matrix_horizontal(self):
    #     # self.slope_matrix = Matrix(self.nrow-1, self.ncol-1)

    #     for row in self.data:
    #         print(list(starmap(sub, pairwise(row))))

    # def slope_matrix_vertical(self):

        
                
         
if __name__ == "__main__":
    
    test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    test_output = advent_of_code_10a(test_input)
    print(f"{test_output}")
    assert test_output == 36

    with open("../data/advent_of_code10/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code_10a(puzzle_input)
    print(f"{puzzle_output}")