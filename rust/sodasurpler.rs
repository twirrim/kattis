use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let input = stdin.lock().lines().next().unwrap().unwrap();
	let split = input.split(" ").flat_map(str::parse::<f32>).collect::<Vec<_>>();;
	let mut empty = split[0];
	let mut found = split[1];
	let need = split[2];
	let mut drunk = 0.0;
	while empty + found >= need {
        empty = empty + found;
        found = 0.0;
        let drunk_this_round = (empty / need).floor();
        empty = empty - (drunk_this_round * need);
        drunk += drunk_this_round;
        empty += drunk_this_round;
    }
    println!("{}", drunk as i32);
}
