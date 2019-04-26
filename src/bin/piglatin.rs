use std::io::{self, BufRead, Write};

fn is_vowel(letter: u8) -> bool {
    // Strings are utf8.
    b"aeiouy".contains(&letter)
}

fn pig_word(word: &str) -> String {
    let mut index = 0;
    for &letter in word.as_bytes() {
        if is_vowel(letter) {
            if index == 0 {
                return format!("{}{}", word, "yay");
            } else {
                let (tailit, headit) = word.split_at(index);
                return format!("{}{}ay", headit, tailit);
            }
        }
        index += 1;
    }
    word.to_string()
}

fn folder(mut current: String, next: String) -> String {
    if !current.is_empty() {
        current.push(' ');
    }
    current.push_str(&next);
    current
}

fn main() {
    // set things up
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut out_lock = stdout.lock();

    for raw_line in stdin.lock().lines() {
        let line = raw_line.unwrap();
        writeln!(
            out_lock,
            "{}",
            line.split_whitespace()
                .map(pig_word)
                .fold(String::new(), folder)
        )
        .unwrap();
    }
}
