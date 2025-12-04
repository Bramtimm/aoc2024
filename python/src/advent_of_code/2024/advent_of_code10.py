from python.src.advent_of_code.utils import Matrix


def advent_of_code_10(puzzle_input: str, max_height: int=9, exercise: str = 'a') -> int:

    puzzle_input = puzzle_input.split()
    puzzle_input = [list(line) for line in puzzle_input]
    
    nrows = len(puzzle_input)
    ncols = len(puzzle_input[0])

    puzzle_matrix = TopoMatrix(nrow = nrows, ncol = ncols)
    
    for row in range(0, nrows):
        for col in range(0, ncols):
            puzzle_matrix[row, col] = int(puzzle_input[row][col])

    pos_hikes = []
    for trailhead_location in puzzle_matrix.trailhead_locations:
        
        trajectories = []
       
        def recursively_traverse(current_position: tuple, current_trajectory: list[tuple]):
            possible_steps = puzzle_matrix.traverse_from_position(current_position)
            if not possible_steps:
                trajectories.append(current_trajectory)
                return
            for next_position in possible_steps:
                    recursively_traverse(next_position, current_trajectory + [next_position])
      
        recursively_traverse(trailhead_location, [trailhead_location])

        
        if exercise == 'a':
            pos_reachable_peaks = {tuple(item) for trajectory in trajectories for item in set(trajectory).intersection(puzzle_matrix.trailpeak_locations)}
            pos_hikes.append(len(pos_reachable_peaks))
        elif exercise == 'b': 
            trajectory_lengths = [len(trajectory) for trajectory in trajectories]
            full_trajectories = sum([length==max_height+1 for length in trajectory_lengths])
            pos_hikes.append(full_trajectories)

    return sum(pos_hikes)


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
    
    def traverse_from_position(self, position: tuple) -> list[tuple]:

        possible_steps = []
        start_row, start_col = position
        start_height = self.data[start_row][start_col]

        # left - up - right - down
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for row, col in directions:
            new_row, new_col = start_row + row, start_col + col
            if 0 <= new_row < self.nrow and 0 <= new_col < self.ncol:
                if self.data[new_row][new_col] - start_height == 1:
                    possible_steps.append((new_row, new_col))
        
        return possible_steps
        
                
         
if __name__ == "__main__":
    
    test_input = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    test_output = advent_of_code_10(test_input, exercise = 'a')
    print(f"{test_output}")
    assert test_output == 36

    with open("../data/advent_of_code10/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code_10(puzzle_input, exercise = 'a')
    print(f"{puzzle_output}")

    test_output = advent_of_code_10(test_input, exercise = 'b')
    print(f"{test_output}")
    assert test_output == 81

    puzzle_output = advent_of_code_10(puzzle_input, exercise = 'b')
    print(f"{puzzle_output}")