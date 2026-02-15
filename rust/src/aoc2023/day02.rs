use regex::Regex;

pub fn advent_of_code2(puzzle_input: &str, bag: Vec<(i32, i32, i32)>) -> i32 {
    let game_re: Regex = Regex::new(r"([0-9]+\b):").unwrap();
    let color_re: Regex = Regex::new(r"(\d+) (red|green|blue)").unwrap();

    let (red, green, blue) = bag[0];

    let mut total = 0;
    for line in puzzle_input.lines() {
        if let Some(caps) = game_re.captures(line) {
            let game_id: i32 = caps[1].parse().unwrap();
            let mut valid_game = true;

            for round in line.split(';') {
                for cap in color_re.captures_iter(round) {
                    let count: i32 = cap[1].parse().unwrap();
                    let color = &cap[2];

                    let is_valid = match color {
                        "red" => count <= red,
                        "green" => count <= green,
                        "blue" => count <= blue,
                        _ => true,
                    };

                    if !is_valid {
                        valid_game = false;
                        break;
                    }
                }
            }
            if valid_game {
                total += game_id;
            }
        }
    }
    total
}
