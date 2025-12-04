from dataclasses import dataclass
from python.src.advent_of_code.utils import Matrix

@dataclass
class Region:
    area: int
    perimeter: int


def advent_of_code12a(input_str: str) -> int:

    input_str = input_str.split()
    input_str = [list(line) for line in input_str]


    nrows = len(input_str)
    ncols = len(input_str[0])

    input_matrix = Matrix(nrows, ncols)
    
    for row in range(0, nrows):
        for col in range(0, ncols):
            input_matrix[row, col] = input_str[row][col]

    input_matrix.print_matrix()

    return 0

if __name__=="__main__":
    
    test_input1 = """AAAA
BBCD
BBCC
EEEC"""

    test_result1 = advent_of_code12a(test_input1)
    assert test_result1==772

    test_input2 = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

    test_result2 = advent_of_code12a(test_input2)
    assert test_result2==1930

    with open("../data/advent_of_code12/puzzle_input.txt", 'r') as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code12a(puzzle_input)
    print(f"puzzle_output is: {puzzle_output}")
    