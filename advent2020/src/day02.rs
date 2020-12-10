#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

struct Password {
    low: u8,
    high: u8,
    letter: char,
    password: String,
}

fn is_valid_part1(entry: &Password) -> bool {
    let total = entry.password.matches(entry.letter).count() as u8;
    if total >= entry.low && total <= entry.high {
        return true;
    }
    return false;
}

fn is_valid_part2(entry: &Password) -> bool {
    let low = entry.password.chars().nth((entry.low - 1).into()).unwrap();
    let high = entry.password.chars().nth((entry.high - 1).into()).unwrap();
    if (low == entry.letter) != (high == entry.letter) {
        return true;
    }
    return false;
}

fn main() {
    let f = File::open("../day02/input").unwrap();
    let file = BufReader::new(&f);
    let mut part1 = 0;
    let mut part2 = 0;
    for line in file.lines() {
        let mut c = 0;
        let mut entry: Password = Password {
            low: 0,
            high: 0,
            letter: 'a',
            password: "a".to_string(),
        };
        for zbr in line.unwrap().split(" ").collect::<Vec<_>>() {
            if c == 0 {
                let tmp2 = zbr.split("-").collect::<Vec<_>>();
                entry.low = tmp2[0].parse::<u8>().clone().unwrap();
                entry.high = tmp2[1].parse::<u8>().clone().unwrap();
            }
            if c == 1 {
                entry.letter = zbr.chars().nth(0).clone().unwrap();
            }
            if c == 2 {
                entry.password = zbr.to_string();
            }
            c += 1;
        }
        if is_valid_part1(&entry) {
            part1 += 1;
        }
        if is_valid_part2(&entry) {
            part2 += 1;
        }
    }
    println!("part1: {}", part1);
    println!("part2: {}", part2);
}

#[bench]
fn bench_day02(b: &mut test::Bencher) {
    b.iter(|| main());
}
