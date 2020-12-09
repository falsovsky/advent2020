#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn toboggan(entries: Vec<String>, xplus: u32, yplus: u32) -> u32 {
    let mut x = 0;
    let mut y = 0;
    let mut trees = 0;
    let gridwidth = entries[0].chars().count() as u32;
    while y < entries.len() as u32 {
        x += xplus;
        y += yplus;
        x %= gridwidth;
        if y < entries.len() as u32 && entries[y as usize].chars().nth(x as usize).unwrap() == '#' {
            trees += 1
        }
    }
    return trees;
}

fn main() {
    let mut entries: Vec<String> = Vec::new();
    let f = File::open("../day03/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        entries.push(line.unwrap());
    }

    println!("part1: {}", toboggan(entries.clone(), 3, 1));

    let mut part2: u64 = 0;
    let slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];
    for slope in &slopes {
        if part2 == 0 {
            part2 = toboggan(entries.clone(), slope[0], slope[1]) as u64;
        } else {
            part2 *= toboggan(entries.clone(), slope[0], slope[1]) as u64;
        }
    }
    println!("part2: {}", part2);
}

#[bench]
fn bench_day03(b: &mut test::Bencher) {
    b.iter(|| main());
}
