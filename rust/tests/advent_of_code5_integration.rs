use advent_of_code_lib::advent_of_code5::*;
use std::fs;

#[test]
fn test_advent_of_code5a() {
    let file_path: &str = "../data/advent_of_code5/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");
    let result = advent_of_code5a(&contents);
    assert_eq!(result, 5108)
}
