from utils import Matrix
from itertools import combinations

def advent_of_code8a(puzzle_input: str) -> int:


    puzzle_input = puzzle_input.split()
    puzzle_input = [list(line) for line in puzzle_input]

    puzzle_matrix = Matrix(nrow=len(puzzle_input), ncol = len(puzzle_input[0]))
    antinode_matrix = Matrix(nrow=len(puzzle_input), ncol = len(puzzle_input[0]))

    for row in range(0, len(puzzle_input)):
        for col in range(0, len(puzzle_input[0])):
            puzzle_matrix[row, col] = puzzle_input[row][col]

    unique_frequencies = puzzle_matrix.get_unique_items(exclude = ["."])

    def _find_antinodes(puzzle_matrix: Matrix, antinode_matrix: Matrix, unique_frequencies = list) -> Matrix:
        """In particular, an antinode occurs at any point that is perfectly in line with two antennas of the same frequency - but only when one of the antennas is twice as far away as the other.
        This means that for any pair of antennas with the same frequency, there are two antinodes, one on either side of them.
        """
        antinode = []
        for freq in unique_frequencies:
            antena_position_sets = []

            # find all positions of the antennas with the same frequency
            for row in range(0, puzzle_matrix.nrow):
                for col in range(0, puzzle_matrix.ncol):
                    if puzzle_matrix[row, col] == freq:
                        antena_position_sets.append((row, col))

            # find all antinode positions
            for combination in combinations(antena_position_sets, 2):
                pos1, pos2 = combination

                def _sub_tuple(t1, t2):
                    # Place the node so that t2 is twice as far from t1
                    return tuple(2 * b - a for a, b in zip(t1, t2))
                
                def _add_tuple(t1, t2):
                    # Place the node so that t1 is twice as far from t2
                    return tuple(2 * a - b for a, b in zip(t1, t2))
                
                antinode.append(_sub_tuple(pos1, pos2))
                antinode.append(_add_tuple(pos1, pos2))

        for antinode_pos in antinode:
            row, col = antinode_pos

            if row >= 0 and row < puzzle_matrix.nrow and col >= 0 and col < puzzle_matrix.ncol:
                antinode_matrix[row, col] = "#"
        
        return antinode_matrix
    
    antinode_matrix = _find_antinodes(puzzle_matrix, antinode_matrix, unique_frequencies)

    return antinode_matrix.count_nr_of_item(item="#")

                
if __name__ == "__main__":

    tst_input = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

    tst_output = advent_of_code8a(tst_input)
    assert tst_output==14

    with open("../data/advent_of_code8/puzzle_input.txt", "r") as f:
        puzzle_input = f.read()

    puzzle_output = advent_of_code8a(puzzle_input)
    print(f"puzzle_output of aoc8a is: {puzzle_output}")

