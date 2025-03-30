use std::collections::{BTreeSet, HashMap, HashSet};

pub fn advent_of_code23a(input_str: &str) -> i32 {
    let mut edge_list: HashMap<&str, Vec<&str>> = HashMap::new();
    let mut three_inter_connected_sets: HashSet<BTreeSet<&str>> = HashSet::new();

    for line in input_str.lines() {
        let mut split = line.split("-");
        let lhs = split.next().unwrap();
        let rhs = split.next().unwrap();

        edge_list.entry(lhs).or_insert_with(Vec::new).push(rhs);
        edge_list.entry(rhs).or_insert_with(Vec::new).push(lhs);
    }


    // iterate over the HashMap
    for (key, values) in &edge_list {
        // create combination of key and two values (i, j) if hashmap key starts with "t"
        if key.starts_with("t") {
            for i in 0..values.len() {
                for j in i + 1..values.len() {
                    // create combination of key and two values (i, j)
                    let mut inter_connected_set: BTreeSet<&str> = BTreeSet::new();
                    inter_connected_set.insert(*key);
                    inter_connected_set.insert(values[i]);

                    // check that the other key also has values[i] so they are interconnected
                    if edge_list.get(values[i]).unwrap().contains(&values[j]) {
                        inter_connected_set.insert(values[j]);
                    }
                    // only add to the set if it has 3 elements
                    if inter_connected_set.len() == 3 {
                        three_inter_connected_sets.insert(inter_connected_set);
                    }
                }
            }
        }
    }

    let result: i32 = three_inter_connected_sets.len() as i32;

    result
}
