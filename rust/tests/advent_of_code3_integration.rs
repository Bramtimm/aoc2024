use advent_of_code_lib::advent_of_code3::*;
use std::fs;

#[test]
fn test_advent_of_code3a_integration() {
    let file_path: &str = "../data/advent_of_code3/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let result: i32 = advent_of_code3a(&contents);
    assert_eq!(result, 169021493);
}

#[test]
fn test_advent_of_code3b_integration() {
    let file_path: &str = "../data/advent_of_code3/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let result: i32 = advent_of_code3b(&contents);
    assert_eq!(result, 111762583);
}
