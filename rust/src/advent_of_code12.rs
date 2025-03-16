use crate::advent_of_code4::Matrix;
;


pub fn advent_of_code12a(mut input_str: &str) -> i32 {
    
    let mut ncols: usize = 0;
    let mut nrows: usize = 0;

    for line in input_str.lines() {
        println!("{}", line);
        nrows = line.len();
        ncols += 1;
    }

    let mut puzzle_matrix = Matrix::new(nrows, ncols, ' ');

    for line in input_str.lines() {
        let mut col_idx = 0;
        for c in line.chars() {
            matrix.set(row_idx, col_idx, c);
            col_idx += 1;
        }
        row_idx += 1;

    println!("nrows: {}, ncols: {}", nrows, ncols);
    println!()
}
