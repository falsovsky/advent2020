#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn xmas(cipher: &Vec<u64>, size: u64) -> u64 {
    for idx in size..cipher.len() as u64 {
        let mut calc: Vec<u64> = Vec::new();
        for x in idx - size..idx {
            for y in x + 1..idx {
                let value = cipher[x as usize] + cipher[y as usize];
                calc.push(value);
            }
        }
        if calc.contains(&cipher[idx as usize]) == false {
            return cipher[idx as usize];
        }
    }
    return 0;
}

fn xmas2(cipher: &Vec<u64>, target: u64) -> u64 {
    let cipherlen = cipher.len() as u64;
    for idx1 in 0..cipherlen as u64 {
        let mut numbers: Vec<u64> = Vec::new();
        let mut total: u64 = 0;

        let val1 = cipher[idx1 as usize];
        numbers.push(val1);
        total += val1;

        for idx2 in idx1 + 1..cipherlen as u64 {
            let val2 = cipher[idx2 as usize];
            numbers.push(val2);
            total += val2;

            if total == target {
                numbers.sort();
                return numbers[0] + numbers[numbers.len() - 1]
            }
        }
    }
    return 0;
}

fn main() {
    let mut cipher: Vec<u64> = Vec::new();
    let f = File::open("../day09/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        cipher.push(line.unwrap().parse::<u64>().unwrap());
    }

    let part1 = xmas(&cipher, 25);
    println!("part1 {}", part1);
    let part2 = xmas2(&cipher, part1);
    println!("part2 {}", part2);
}

#[bench]
fn bench_day09(b: &mut test::Bencher) {
    b.iter(|| main());
}
