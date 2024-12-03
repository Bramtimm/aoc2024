use crate::advent_of_code1::advent_of_code1;

pub mod advent_of_code1;
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_advent_of_code1() {

        let mut vec_1 = vec![3, 4, 2, 1, 3, 3];    
        let mut vec_2 = vec![4, 3, 5, 3, 9, 3];
        let result: i32 = advent_of_code1(&mut vec_1, &mut vec_2); 
        assert_eq!(result, 11);
    }


}


pub fn test() {
    println!("Test");
}
