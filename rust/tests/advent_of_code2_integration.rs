use advent_of_code_lib::advent_of_code2::*;
use std::fs;

#[test]
fn test_advent_of_code2_integration() {
    let file_path: &str = "../data/advent_of_code2/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let mut vec_1: Vec<Vec<i32>> = Vec::new();

    for line in contents.lines() {
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        vec_1.push(numbers);
    }
    let result: i32 = advent_of_code2a(&mut vec_1);
    assert_eq!(result, 257);

    let result: i32 = advent_of_code2b(&mut vec_1);
    assert_eq!(result, 328)
}
