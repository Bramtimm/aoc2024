use advent_of_code_lib::aoc2023::day02::*;
use std::fs;

#[test]
fn test_advent_of_code2_integration() {
    let file_path: &str = "../data/2023/advent_of_code2/puzzle_input.txt";

    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let bag = vec![(12 ,13, 14)];
    let result: i32 = advent_of_code2(&contents, bag);
    assert_eq!(result, 2505);
}
