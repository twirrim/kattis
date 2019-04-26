use std::io::{self, BufRead};

// This is a longest increasing sequence question.
// Strings in rust are easily read as vectors of characters.  Algorithm and explanation here:
// http://www.algorithmist.com/index.php/Longest_Increasing_Subsequence
// function lis_length( a )
//     n := a.length
//     q := new Array(n)
//     for k from 0 to n:
//         max := 0;
//         for j from 0 to k, if a[k] > a[j]:
//             if q[j] > max, then set max = q[j].
//         q[k] := max + 1;
//     max := 0
//     for i from 0 to n:
//         if q[i] > max, then set max = q[i].
//     return max;

fn lis_length(a: Vec<u8>) -> usize {
    let n = a.len();
    let mut q = vec![0; n];
    for k in 0..n {
        let mut max = 0;
        for j in 0..k {
            if a[k] > a[j] && q[j] > max {
                max = q[j];
            };
        }
        q[k] = max + 1;
    }
    let mut max = 0;
    for i in 0..n {
        if q[i] > max {
            max = q[i];
        }
    }
    max
}

fn main() {
    let stdin = io::stdin();

    // Get the Input
    let data = stdin.lock().lines().next().unwrap().unwrap();
    let line = data.into_bytes();
    let result = 26 - lis_length(line);
    println!("{:?}", result);
}
