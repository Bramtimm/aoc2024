use regex::Regex;

struct Matrix<T> {
    cols: usize,
    rows: usize,
    data: Vec<Vec<T>>,
}

impl<T> Matrix<T> {
    fn new(rows: usize, cols: usize, initial: T) -> Self
    where
        T: Clone,
    {
        let mut data = Vec::with_capacity(rows);
        for _ in 0..rows {
            data.push(vec![initial.clone(); cols]);
        }

        Matrix { rows, cols, data }
    }

    fn set(&mut self, row: usize, col: usize, value: T) {
        self.data[row][col] = value;
    }

    fn get_diagional(&self) -> Vec<T>
    where
        T: Clone,
    {
        let mut diag = Vec::new();
        for i in 0..self.rows {
            diag.push(self.data[i][i].clone());
        }
        diag
    }

    fn get_reverse_diagional(&self) -> Vec<T>
    where
        T: Clone,
    {
        let mut diag = Vec::new();
        for i in 0..self.rows {
            diag.push(self.data[i][self.cols - i - 1].clone());
        }
        diag
    }
}

pub fn advent_of_code4a(input_str: &str) -> i32 {
    // TODO read in string

    let mut cols: usize = 0;
    let mut rows: usize = 0;
    for line in input_str.lines() {
        println!("{}", line);
        rows = line.len();
        cols += 1;
    }

    let mut matrix = Matrix::new(rows, cols, ' ');

    let mut row_idx = 0;
    for line in input_str.lines() {
        let mut col_idx = 0;
        for c in line.chars() {
            matrix.set(row_idx, col_idx, c);
            col_idx += 1;
        }
        row_idx += 1;
    }

    let pattern = Regex::new(r"XMAS").unwrap();
    let reverse_pattern = Regex::new(r"SAMX").unwrap();
    let pattern_length = "XMAS".len();

    let mut count = 0;

    for i in 0..matrix.rows {
        let row = matrix.data[i].iter().collect::<String>();
        let matches: Vec<_> = pattern.find_iter(&row).collect();
        count += matches.len();

        let matches: Vec<_> = reverse_pattern.find_iter(&row).collect();
        count += matches.len();
    }

    for i in 0..matrix.cols {
        let col = matrix.data.iter().map(|row| row[i]).collect::<String>();
        let matches: Vec<_> = pattern.find_iter(&col).collect();
        count += matches.len();

        let matches: Vec<_> = reverse_pattern.find_iter(&col).collect();
        count += matches.len();
    }

    for i in 0..matrix.rows {
        for j in 0..matrix.cols {
            if i + pattern_length - 1 < matrix.rows && j + pattern_length - 1 < matrix.cols {
                let mut sub_matrix = Matrix::new(pattern_length, pattern_length, '_');

                for row_index in 0..pattern_length {
                    for col_index in 0..pattern_length {
                        sub_matrix.set(
                            row_index,
                            col_index,
                            matrix.data[i + row_index][j + col_index],
                        );
                    }
                }
                let diag = sub_matrix.get_diagional().iter().collect::<String>();
                let reverse_diag = sub_matrix
                    .get_reverse_diagional()
                    .iter()
                    .collect::<String>();

                let matches: Vec<_> = pattern.find_iter(&diag).collect();
                let reverse_pattern_matches: Vec<_> = reverse_pattern.find_iter(&diag).collect();
                count += matches.len();
                count += reverse_pattern_matches.len();

                let reverse_matches: Vec<_> = pattern.find_iter(&reverse_diag).collect();
                let reverse_reverse_matches: Vec<_> =
                    reverse_pattern.find_iter(&reverse_diag).collect();
                count += reverse_matches.len();
                count += reverse_reverse_matches.len();
            }
        }
    }

    println!("{:?}", count);
    println!("{:?}", matrix.data);

    count as i32
}
