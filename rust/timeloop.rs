use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
    let count = input.parse::<u8>().unwrap();
    for x in 1..count+1 {
        println!("{} Abracadabra", x);
    }
}
