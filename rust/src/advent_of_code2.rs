pub fn advent_of_code2a(input_vec: &mut Vec<Vec<i32>>) -> i32 {
    let result_vec: Vec<bool> = input_vec.iter_mut().map(|vec| is_safe(vec)).collect();

    let result: i32 = result_vec.iter().map(|&x| x as i32).sum();

    result
}

fn is_safe(input_vec: &mut Vec<i32>) -> bool {
    let pairwsise_difference: Vec<i32> = input_vec
        .windows(2)
        .map(|windows| windows[1] - windows[0])
        .collect();

    let all_increasing_and_123: bool = pairwsise_difference.iter().all(|&x| x >= 1 && x <= 3);
    let all_decreasing_and_123: bool = pairwsise_difference.iter().all(|&x| x >= -3 && x <= -1);

    all_increasing_and_123 | all_decreasing_and_123
}
