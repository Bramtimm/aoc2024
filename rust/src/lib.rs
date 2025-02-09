pub mod advent_of_code1;
pub mod advent_of_code11;
pub mod advent_of_code2;
pub mod advent_of_code3;
pub mod advent_of_code4;
pub mod advent_of_code5;
#[cfg(test)]
mod tests {
    use crate::advent_of_code1::*;
    use crate::advent_of_code11::*;
    use crate::advent_of_code2::*;
    use crate::advent_of_code3::*;
    use crate::advent_of_code4::*;
    use crate::advent_of_code5::*;

    #[test]
    fn test_advent_of_code1() {
        let mut vec_1: Vec<i32> = vec![3, 4, 2, 1, 3, 3];
        let mut vec_2: Vec<i32> = vec![4, 3, 5, 3, 9, 3];
        let result: i32 = advent_of_code1(&mut vec_1, &mut vec_2);
        assert_eq!(result, 11);
    }

    #[test]
    fn test_advent_of_code1b() {
        let mut vec_1: Vec<i32> = vec![3, 4, 2, 1, 3, 3];
        let mut vec_2: Vec<i32> = vec![4, 3, 5, 3, 9, 3];
        let result: i32 = advent_of_code1b(&mut vec_1, &mut vec_2);
        assert_eq!(result, 31);
    }

    #[test]
    fn test_advent_of_code2a() {
        let mut vec_1: Vec<Vec<i32>> = vec![
            vec![7, 6, 4, 2, 1],
            vec![1, 2, 7, 8, 9],
            vec![9, 7, 6, 2, 1],
            vec![1, 3, 2, 4, 5],
            vec![8, 6, 4, 4, 1],
            vec![1, 3, 6, 7, 9],
        ];
        let result: i32 = advent_of_code2a(&mut vec_1);
        assert_eq!(result, 2);
    }

    #[test]
    fn test_advent_of_code2b() {
        let mut vec_1: Vec<Vec<i32>> = vec![
            vec![7, 6, 4, 2, 1],
            vec![1, 2, 7, 8, 9],
            vec![9, 7, 6, 2, 1],
            vec![1, 3, 2, 4, 5],
            vec![8, 6, 4, 4, 1],
            vec![1, 3, 6, 7, 9],
        ];
        let result: i32 = advent_of_code2b(&mut vec_1);
        assert_eq!(result, 4);
    }

    #[test]
    fn test_advent_of_code3a() {
        let input_str: &str =
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
        let result: i32 = advent_of_code3a(input_str);
        assert_eq!(result, 161);
    }

    #[test]
    fn test_advent_of_code3b() {
        let input_str: &str =
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))";
        let result: i32 = advent_of_code3b(input_str);
        assert_eq!(result, 48)
    }

    #[test]
    fn test_advent_of_code4a() {
        let input_str: &str = "MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX";
        let result: i32 = advent_of_code4a(input_str);
        assert_eq!(result, 18)
    }

    #[test]
    fn test_advent_of_code5a() {
        let input_str: &str = "47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47";

        let result: i32 = advent_of_code5a(input_str);
        assert_eq!(result, 143);
    }

    #[test]
    fn test_advent_of_code11() {
        let input_str: &str = "125 17";
        let result: i64 = advent_of_code11(input_str, 25);
        assert_eq!(result, 55312)
    }
}

pub fn test() {
    println!("Test");
}
