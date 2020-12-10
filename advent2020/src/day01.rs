#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let f = File::open("../day01/input").unwrap();
    let file = BufReader::new(&f);
    let mut entries: Vec<_> = Vec::new();
    for line in file.lines() {
        entries.push(line.unwrap().parse::<u32>().unwrap());
    }

    let mut part1 = false;
    'outer: for x in &entries {
        for y in &entries {
            if !part1 && x + y == 2020 {
                println!("part1: {}", x * y);
                part1 = true;
            }
            if x + y > 2020 {
                continue;
            }
            for z in &entries {
                if part1 && x + y + z == 2020 {
                    println!("part2: {}", x * y * z);
                    break 'outer;
                }
            }
        }
    }
}

#[bench]
fn bench_day01(b: &mut test::Bencher) {
    b.iter(|| main());
}
