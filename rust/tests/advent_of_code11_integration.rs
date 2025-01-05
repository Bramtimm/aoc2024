use advent_of_code_lib::advent_of_code11::*;
use std::fs;

#[test]
fn test_advent_of_code11_integration() {
    let file_path: &str = "../data/advent_of_code11/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let result: i64 = advent_of_code11(&contents, 25);
    assert_eq!(result, 184927);

    // let result: i64 = advent_of_code11(&contents, 75);
    // assert_eq!(result, 220357186726677)
}
