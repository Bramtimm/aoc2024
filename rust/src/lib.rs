pub mod advent_of_code1;
pub mod advent_of_code2;
pub mod advent_of_code3;
#[cfg(test)]
mod tests {
    use crate::advent_of_code1::*;
    use crate::advent_of_code2::*;
    use crate::advent_of_code3::*;

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
}

pub fn test() {
    println!("Test");
}
