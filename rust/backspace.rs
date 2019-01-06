use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();

    // Get the Input
    let data = stdin.lock().lines().next().unwrap().unwrap();
    let line = data.into_bytes();
    let mut output = vec!();
    for character in &line{
        // 60 is the < symbol
        if *character == 60 as u8{
            output.pop();
        } else {
            output.push(*character);
        }
    }
    let s = String::from_utf8(output).unwrap();
    println!("{}", s);
}
