use regex::Regex;

pub fn advent_of_code3a(input_str: &str) -> i32 {

    let re: Regex = Regex::new(r"mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\)").unwrap();

    let groups: Vec<(&str, &str)> = re.captures_iter(input_str).map(|caps|{
        
        let x: &str = caps.name("x").unwrap().as_str();
        let y: &str = caps.name("y").unwrap().as_str();
        (x, y)
    }).collect();

    let result_vec: Vec<i32> = groups.iter().map(|&cap|{
       let (x, y) =  cap;
       let x: i32 = x.parse().expect("failed to parse");
       let y: i32 = y.parse().expect("failed to parse");
       let mul_res: i32 = x*y;
       mul_res
    }).collect();

    let result: i32 = result_vec.iter().sum();
    result
}
