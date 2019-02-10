use std::io::{self, BufRead};
use std::collections::HashSet;
use std::collections::HashMap;
use std::collections::BTreeMap;

fn main() {
    // set things up
    let stdin = io::stdin();
    let mut unique_word_list = HashSet::new();
    let mut users_words = HashMap::new();
    let mut word_count = BTreeMap::new();
    let _throwaway = stdin.lock().lines().next().unwrap().unwrap();

    for raw_line in stdin.lock().lines() {
        let line = raw_line.unwrap();
        let mut split = line.split(' ');
        let user = split.next().unwrap();
        for entry in split{
            let user_unique_words = users_words.entry(String::from(user)).or_insert(HashSet::new());
            let count = word_count.entry(String::from(entry)).or_insert(0);
            *count += 1;
            unique_word_list.insert(String::from(entry));
            user_unique_words.insert(String::from(entry));
        }
    }
    // we only care about words used by all users, so we figure out an intersection of all the hash
    // sets
    

    for (_user, words) in &users_words {
        unique_word_list = unique_word_list.intersection(&words).cloned().collect();
    }
    if unique_word_list.len() > 0 {
        let mut count_vec: Vec<(&String, &usize)> = word_count.iter().collect();
        eprintln!("{:?}", count_vec);
        count_vec.sort_by(|a, b| a.1.cmp(b.1).reverse());
        for word in count_vec {
            if unique_word_list.contains(word.0) {
                println!("{}", word.0);
            }
        }
    } else {
        println!("ALL CLEAR");
    };
}
