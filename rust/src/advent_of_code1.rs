pub fn advent_of_code1(vec_1: &mut Vec<i32>, vec_2: &mut Vec<i32>) -> i32 {
    vec_1.sort();
    vec_2.sort();

    let distance_vec: Vec<i32> = vec_1
        .iter_mut()
        .zip(vec_2.iter_mut())
        .map(|(elem_a, elem_b)| *elem_a - *elem_b)
        .collect();

    let distance: i32 = distance_vec.iter().map(|&x| x.abs()).sum();
    distance
}

pub fn advent_of_code1b(vec_1: &mut Vec<i32>, vec_2: &mut Vec<i32>) -> i32 {
    
    let mut similarity_score: i32 = 0;

    for element in vec_1.iter() {
        let count: i32 = vec_2.iter().filter(|&n| *n == *element).count().try_into().unwrap(); 
        similarity_score += element * count;
    }

    similarity_score
}

