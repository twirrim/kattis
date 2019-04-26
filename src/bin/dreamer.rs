use std::collections::HashSet;
use std::io::{self, BufRead};

// from https://en.wikipedia.org/wiki/Heap%27s_algorithm
fn permutations(n: usize, mut a: Vec<usize>) -> HashSet<Vec<usize>> {
    let mut c = Vec::with_capacity(n);
    let mut output = HashSet::new();
    for _ in 0..n {
        c.push(0);
    }
    output.insert(a.to_vec());
    let mut i = 0;
    while i < n {
        if c[i] < i {
            if i & 1 == 0 {
                // if i is even
                let zero = a[0];
                a[0] = a[i];
                a[i] = zero;
            } else {
                let zero = a[c[i]];
                a[c[i]] = a[i];
                a[i] = zero;
            }
            // polluting this with application specific logic to avoid expensive hashing operations
            if a[0] >= 2 && a[4] <= 1 && a[6] <= 3 {
                output.insert(a.to_vec());
            };
            c[i] += 1;
            i = 0;
        } else {
            c[i] = 0;
            i += 1;
        }
    }
    output
}

fn is_leap_year(year: usize) -> bool {
    if year % 4 != 0 {
        return false;
    }
    if year % 400 == 0 {
        return true;
    }
    if year % 100 == 0 {
        return false;
    }
    true
}

fn is_valid_date(year: usize, month: usize, day: usize) -> bool {
    // Quick and easy filters?
    if year < 2000 {
        return false;
    }
    if month > 12 || month == 0 {
        return false;
    }
    if day > 31 || day == 0 {
        return false;
    }
    if [1 as usize, 3, 5, 7, 8, 10, 12].contains(&month) {
        return day <= 31;
    } else if [4 as usize, 6, 9, 11].contains(&month) {
        return day <= 30;
    } else if month == 2 {
        if is_leap_year(year) {
            return day <= 29;
        }
        return day <= 28;
    }
    false
}

fn main() {
    let stdin = io::stdin();

    // we can ignore the first line
    let _ = stdin.lock().lines().next().unwrap().unwrap();

    // Iterate over the rest
    for line in stdin.lock().lines().map(|l| l.unwrap()) {
        // Convert to a vector of integers, filtering out any whitespace automatically
        let chars: Vec<usize> = line
            .chars()
            .filter_map(|x| x.to_string().parse::<usize>().ok())
            .collect();

        let mut count = 0;
        let mut earliest = 99999999; // eww?
        for perm in permutations(chars.len(), chars) {
            // Can this be done neater?  maybe flatten_map?  Would that be any quicker?
            // Should I just be flattening the entire thing?
            let year = (perm[0] * 1000) + (perm[1] * 100) + (perm[2] * 10) + perm[3];
            let month = (perm[4] * 10) + perm[5];
            let day = (perm[6] * 10) + perm[7];
            if is_valid_date(year, month, day) {
                let combined = (year * 10000) + (month * 100) + day;
                if combined < earliest {
                    earliest = combined;
                };
                count += 1;
            }
        }
        let digits: Vec<_> = earliest
            .to_string()
            .chars()
            .map(|d| d.to_digit(10).unwrap())
            .collect();
        let early_year = (digits[0] * 1000) + (digits[1] * 100) + (digits[2] * 10) + digits[3];
        let early_month = (digits[4] * 10) + digits[5];
        let early_day = (digits[6] * 10) + digits[7];
        if count > 0 {
            println!(
                "{} {:02} {:02} {}",
                count, early_day, early_month, early_year
            );
        } else {
            println!("{}", count);
        }
    }
}
