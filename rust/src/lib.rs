pub mod advent_of_code1;
pub mod advent_of_code3;
#[cfg(test)]
mod tests {
    use crate::advent_of_code1::*;
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
    fn test_advent_of_code3a() {
        let input_str: &str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
        let result: i32 = advent_of_code3a(input_str);
        assert_eq!(result, 161);
    }
    
}

pub fn test() {
    println!("Test");
}
