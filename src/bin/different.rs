use std::io::{self, BufRead};

fn main() {
    // set things up
    let stdin = io::stdin();

    for raw_line in stdin.lock().lines() {
        let line = raw_line.unwrap();
        let mut split = line.split(' ');
        let first = split.next().unwrap().parse::<isize>().unwrap();
        let second = split.next().unwrap().parse::<isize>().unwrap();
        let diff = first - second;
        println!("{}", diff.abs());
    }
}
