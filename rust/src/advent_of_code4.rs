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

    //TODO make set logic
    fn set(&mut self, row: usize, col: usize, value: T) {
        self.data[row][col] = value;
    }

    //TODO make get logic
    fn get(&self, row: usize, col: usize) -> &T {
        &self.data[row][col]
    }

    fn 
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

    println!("{:?}", matrix.data);

    18
}
