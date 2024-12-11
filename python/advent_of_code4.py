import re

def advent_of_code4a(test_input: str | list, pattern = 'XMAS') -> int:

    if isinstance(test_input, str):
        puzzle_input = test_input.split()
        puzzle_input = [list(line) for line in puzzle_input]
 
    elif isinstance(test_input, list):
        puzzle_input = [list(line[0]) for line in test_input]


    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])

    puzzle_matrix = Matrix(nrow = nrows, ncol = ncols)
    
    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = puzzle_input[row][col]

    row_count = 0
    col_count = 0
    diag_count = 0
    
    pattern_len = len(list(pattern))
    pattern = rf'{pattern}'
    reverse_pattern = ''.join(reversed(list(pattern)))
    reverse_pattern = rf'{reverse_pattern}'

    for row in range(0, nrows):
        row_count += len(re.findall(pattern = pattern, string = ''.join(puzzle_matrix[row,:])))
        row_count += len(re.findall(pattern = reverse_pattern, string = ''.join(puzzle_matrix[row,:])))
        
    for col in range(0, ncols):

        col_count += len(re.findall(pattern = pattern, string = ''.join(puzzle_matrix.get_column(col))))
        col_count += len(re.findall(pattern = reverse_pattern, string = ''.join(puzzle_matrix.get_column(col))))
        
    for row in range(0, nrows):
         for col in range(0, ncols):
            
            if row+pattern_len-1 in range(0,nrows) and col+pattern_len-1 in range(0,ncols):
                sub_matrix = Matrix(pattern_len, pattern_len, fill='_')   
                for row_index, row2 in enumerate(range(row, row+pattern_len)):
                    for col_index, col2 in enumerate(range(col, col+pattern_len)):
                       
                        sub_matrix[row_index, col_index] = puzzle_input[row2][col2]
                # print(''.join(sub_matrix.get_diagonal()))
                diag_count += len(re.findall(pattern = pattern, string = ''.join(sub_matrix.get_diagonal()))) 
                diag_count += len(re.findall(pattern = pattern, string = ''.join(sub_matrix.get_reverse_diagonal()))) 
                diag_count += len(re.findall(pattern = reverse_pattern, string = ''.join(sub_matrix.get_diagonal()))) 
                diag_count += len(re.findall(pattern = reverse_pattern, string = ''.join(sub_matrix.get_reverse_diagonal()))) 
              
    return row_count + col_count + diag_count


def advent_of_code4b(test_input: str|list, cross_pattern = "MAS") -> int:

    if isinstance(test_input, str):
        puzzle_input = test_input.split()
        puzzle_input = [list(line) for line in puzzle_input]
 
    elif isinstance(test_input, list):
        puzzle_input = [list(line[0]) for line in test_input]

    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])

    puzzle_matrix = Matrix(nrow = nrows, ncol = ncols)
    
    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = puzzle_input[row][col]

    pattern_len = len(list(cross_pattern))
    pattern = rf'{cross_pattern}'
    reverse_pattern = ''.join(reversed(list(pattern)))
    cross_pattern = pattern + (f"|{reverse_pattern}")

    cross_diag_count = 0 
    for row in range(0, nrows):
        for col in range(0, ncols):           
            if row+pattern_len-1 in range(0,nrows) and col+pattern_len-1 in range(0,ncols):
                sub_matrix = Matrix(pattern_len, pattern_len, fill='_')   
                
                for row_index, row2 in enumerate(range(row, row+pattern_len)):
                    for col_index, col2 in enumerate(range(col, col+pattern_len)):
                       
                        sub_matrix[row_index, col_index] = puzzle_input[row2][col2]

                        pattern_on_diagonals =len(re.findall(pattern = cross_pattern, string = ''.join(sub_matrix.get_diagonal()))) + len(re.findall(pattern = cross_pattern, string = ''.join(sub_matrix.get_reverse_diagonal())))

                        if pattern_on_diagonals == 2:
                             cross_diag_count += 1
    
    return cross_diag_count
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

    def get_diagonal(self):

        self.diagonal = []
        for diag_index in range(0, self.nrow):
            self.diagonal.append(self.data[diag_index][diag_index])

        return self.diagonal

    def get_reverse_diagonal(self):
        
        self.reverse_diagonal = []
        
        for diag_index in range(0, self.nrow):
            self.reverse_diagonal.append(self.data[diag_index][self.ncol-diag_index-1])
        return self.reverse_diagonal

    def get_column(self, col_index):
        
        self.column = []
        for i in range(0, self.nrow):
            self.column.append(self.data[i][col_index])

        return self.column
  


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
    print(test_output)
    assert test_output == 18

    with open("../data/advent_of_code4/puzzle_input.txt", "r") as f:
        puzzle_input = [line.split() for line in f if line.strip()]

    
    puzzle_output = advent_of_code4a(puzzle_input)
    print(puzzle_output)
    
    test_output = advent_of_code4b(test_input)
    print(test_output)
    assert test_output == 9

    puzzle_output = advent_of_code4b(puzzle_input)
    print(puzzle_output)

