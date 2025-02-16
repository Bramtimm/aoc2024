use crate::advent_of_code4::Matrix;
use itertools::Itertools;

pub fn advent_of_code8a(puzzle_input: &str) -> i32 {
    let mut cols: usize = 0;
    let mut rows: usize = 0;
    for line in puzzle_input.lines() {
        println!("{}", line);
        rows = line.len();
        cols += 1;
    }

    let mut puzzle_matrix = Matrix::new(rows, cols, ' ');
    let mut antinode_matrix = Matrix::new(rows, cols, ' ');

    for (i, line) in puzzle_input.lines().enumerate() {
        for (j, c) in line.chars().enumerate() {
            puzzle_matrix.set(i, j, c);
        }
    }

    let unique_frequencies = puzzle_matrix.get_unique_items('.');

    fn find_antinode_matrix<'a>(
        puzzle_matrix: &mut Matrix<char>,
        antinode_matrix: &'a mut Matrix<char>,
        unique_frequencies: Vec<char>,
    ) -> &'a mut Matrix<char> {
        let mut antinode: Vec<(i32, i32)> = Vec::new();

        for freq in unique_frequencies {
            let mut antenna_position_sets: Vec<(usize, usize)> = Vec::new();

            // find all positions of the antennas with the same frequency
            for row in 0..puzzle_matrix.rows {
                for col in 0..puzzle_matrix.cols {
                    if puzzle_matrix.get(row, col) == &freq {
                        antenna_position_sets.push((row, col));
                    }
                }
            }

            // find all antinode positions
            for combination in antenna_position_sets.iter().combinations(2) {
                let pos1 = combination[0];
                let pos2 = combination[1];

                let sub_tuple = |t1: &(usize, usize), t2: &(usize, usize)| -> (i32, i32) {
                    // Place the node so that t2 is twice as far from t1
                    (
                        (2 * t2.0 as i32 - t1.0 as i32),
                        (2 * t2.1 as i32 - t1.1 as i32),
                    )
                };

                let add_tuple = |t1: &(usize, usize), t2: &(usize, usize)| -> (i32, i32) {
                    // Place the node so that t1 is twice as far from t2
                    (2 * t1.0 as i32 - t2.0 as i32, 2 * t1.1 as i32 - t2.1 as i32)
                };

                antinode.push(sub_tuple(pos1, pos2));
                antinode.push(add_tuple(pos1, pos2));
            }

            for anti_node in &antinode {
                let (row, col) = anti_node;

                if *row >= 0
                    && *row < puzzle_matrix.rows.try_into().unwrap()
                    && *col >= 0
                    && *col < puzzle_matrix.cols.try_into().unwrap()
                {
                    antinode_matrix.set(
                        (*row).try_into().unwrap(),
                        (*col).try_into().unwrap(),
                        '#',
                    );
                }
            }
        }
        return antinode_matrix;
    }

    let antinode_matrix =
        find_antinode_matrix(&mut puzzle_matrix, &mut antinode_matrix, unique_frequencies);

    antinode_matrix.get_count('#') as i32
}
