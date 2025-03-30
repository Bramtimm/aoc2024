use advent_of_code_lib::advent_of_code23::*;
use std::fs;

#[test]
fn test_advent_of_code23_integration() {
    let file_path: &str = "../data/advent_of_code23/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let result: i32 = advent_of_code23a(&contents);
    println!("Result: {}", result);
    assert_eq!(result, 1512);
}
