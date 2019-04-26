use std::io::{self, BufRead, Write};

fn main() {
    let stdin = io::stdin();
    let _ignore = stdin.lock().lines().next().unwrap().unwrap();
    let stdout = io::stdout();
    let mut out = stdout.lock();
    for line in stdin.lock().lines() {
        let n: Vec<i32> = line
            .unwrap()
            .split(' ')
            .map(|s| s.trim())
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect();
        let s1 = (n[1] * (n[1] + 1)) / 2;
        let s3 = s1 * 2;
        let s2 = s3 - n[1];

        writeln!(out, "{} {} {} {}", n[0], s1, s2, s3).unwrap();
    }
}
