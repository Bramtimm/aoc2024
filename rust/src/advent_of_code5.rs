use regex::Regex;
use std::collections::HashMap;

pub fn advent_of_code5a(puzzle_input: &str) -> i32 {
    // split file for ruleset and input
    let re = Regex::new(r"\n\n").unwrap();

    let mut splits = re.split(puzzle_input);
    let ruleset_str = splits.next().unwrap_or("");
    let input_str = splits.next().unwrap_or("");

    // retrieve rules
    let mut ruleset_dict = HashMap::new();

    for line in ruleset_str.lines() {
        let mut split = line.split("|");
        let lhs = split.next().unwrap().parse::<i32>().unwrap();
        let rhs = split.next().unwrap().parse::<i32>().unwrap();

        ruleset_dict.entry(lhs).or_insert_with(Vec::new).push(rhs);
    }

    // retrieve input_str as vec
    let mut input_vec: Vec<Vec<i32>> = Vec::new();

    for line in input_str.lines() {
        let numbers: Vec<i32> = line.split(',').map(|s| s.parse().unwrap()).collect();
        input_vec.push(numbers);
    }

    // check input_str_ordering based on ruleset
    let mut valid_ordering: Vec<bool> = Vec::new();

    for vector in &input_vec {
        valid_ordering.push(check_ruleset(vector, ruleset_dict.clone()));
    }

    println!("{:?}", valid_ordering);

    // get middle value if it has valid ordering
    let mut middle_values = Vec::new();

    for (index, vector) in input_vec.iter().enumerate() {
        if valid_ordering[index] {
            middle_values.push(get_middle_value(vector))
        }
    }

    // sum values
    middle_values.iter().sum()
}

fn check_ruleset(input_vec: &Vec<i32>, ruleset_dict: HashMap<i32, Vec<i32>>) -> bool {
    for (index, &element) in input_vec.iter().enumerate() {
        // Only check if there is a "next" element
        if index + 1 < input_vec.len() {
            if let Some(rule) = ruleset_dict.get(&element) {
                let next_element = input_vec[index + 1];
                if !rule.contains(&next_element) {
                    return false;
                }
            } else {
                // If there's no rule for an element that does lead to another element, fail
                return false;
            }
        }
        // If this is the last element, we simply do not check for a rule
    }

    true
}

fn get_middle_value(vec: &Vec<i32>) -> i32 {
    let middle_index = vec.len() / 2;
    vec[middle_index]
}
