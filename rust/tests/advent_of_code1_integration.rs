use advent_of_code_lib::advent_of_code1::*;
use std::fs;

#[test]
fn test_advent_of_code1_integration() {
    let file_path: &str = "../data/advent_of_code1/puzzle_input.txt";
    let contents = fs::read_to_string(&file_path).expect("Should have been able to read the file");

    let mut vec_1 = Vec::new();
    let mut vec_2 = Vec::new();

    for line in contents.lines() {
        let numbers: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        vec_1.push(numbers[0]);
        vec_2.push(numbers[1]);
    }

    let distance: i32 = advent_of_code1(&mut vec_1, &mut vec_2);
    assert_eq!(distance, 2769675);

    let similarity: i32 = advent_of_code1b(&mut vec_1, &mut vec_2);
    assert_eq!(similarity, 24643097);
}
