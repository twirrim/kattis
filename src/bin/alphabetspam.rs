use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();

    // Get the Input
    let data = stdin.lock().lines().next().unwrap().unwrap();
    let line = data.into_bytes();
    let length = line.len() as f64;
    let whitespace = b"_";
    let lower = b"abcdefghijklmnopqrstuvwxyz";
    let upper = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let mut whitespace_count = 0.0;
    let mut lower_count = 0.0;
    let mut upper_count = 0.0;
    let mut symbol_count = 0.0;
    for letter in &line {
        if lower.contains(letter) {
            lower_count += 1.0;
        } else if whitespace.contains(letter) {
            whitespace_count += 1.0;
        } else if upper.contains(letter) {
            upper_count += 1.0;
        } else {
            symbol_count += 1.0;
        };
    };
    let ratio_per_letter = 1.0 / length;
    println!("{:.15}\n{:.15}\n{:.15}\n{:.15}",
             ratio_per_letter * whitespace_count,
             ratio_per_letter * lower_count,
             ratio_per_letter * upper_count,
             ratio_per_letter * symbol_count);
}
