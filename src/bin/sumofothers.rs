use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    for line in stdin.lock().lines() {
        let numbers: Vec<i32> = line
            .unwrap()
            .split(' ')
            .map(|s| s.trim())
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect();
        let sum: i32 = numbers.iter().sum();
        for number in &numbers {
            if sum - *number == *number {
                println!("{}", number.to_string());
                break;
            };
        }
    }
}
