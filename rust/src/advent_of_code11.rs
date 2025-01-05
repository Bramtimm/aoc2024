pub fn advent_of_code11(input_str: &str, blinks: i32) -> i64 {
    // str split
    let mut numbers: Vec<i64> = input_str
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let len_numbers: Vec<i64> = numbers.iter_mut().map(|x| blink(*x, blinks)).collect();

    len_numbers.iter().sum()
}

fn blink(element: i64, blinks: i32) -> i64 {
    if blinks == 0 {
        return 1;
    } else if element == 0 {
        return blink(1, blinks - 1);
    } else if element.to_string().len() % 2 == 0 {
        let str_element = element.to_string();
        let len_element = str_element.len();
        let (first_element, second_element) = str_element.split_at(len_element / 2);
        return blink(first_element.parse().unwrap(), blinks - 1)
            + blink(second_element.parse().unwrap(), blinks - 1);
    } else {
        return blink(element * 2024, blinks - 1);
    }
}
