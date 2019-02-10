// Hissing Microphone problem on Kattis
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();

    // Get the Input
    let data = stdin.lock().lines().next().unwrap().unwrap();

    // I doubt it's necessary to do the string conversion, but it's easy.
    if String::from(data).contains("ss") {
        println!("hiss")
    } else {
        println!("no hiss")
    }
}