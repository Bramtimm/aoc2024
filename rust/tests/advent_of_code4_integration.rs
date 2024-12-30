use advent_of_code_lib::advent_of_code4::*;
use std::fs;

#[test]
fn test_advent_of_code4a_integration() {
    let file_path: &str = "../data/advent_of_code4/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let result: i32 = advent_of_code4a(&contents);
    assert_eq!(result, 2639);
}
