use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    // set things up
    let stdin = io::stdin();
    let line = stdin.lock().lines().next().unwrap().unwrap();
    let mut split = line.split(' ');
    let n: usize = split.next().unwrap().parse::<usize>().unwrap();
    let mut found: HashSet<usize> = HashSet::new();
    for raw_line in stdin.lock().lines() {
        found.insert(raw_line.unwrap().parse::<usize>().unwrap());
    }
    for i in 0..n {
        if !found.contains(&i) {
            println!("{}", i.to_string());
        }
    }
    println!("Mario got {} of the dangerous obstacles.", found.len());
}
