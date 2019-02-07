use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();
    // We don't care about the first line
    let _throwaway = iterator.next().unwrap().unwrap();
    let input = iterator.next().unwrap().unwrap();
    let entries = input.split(' ');
    let mut count = 0;
    for entry in entries {
        if entry.parse::<i32>().unwrap() < 0 {
            count += 1;
        }
    };
    println!("{}", count);
}
