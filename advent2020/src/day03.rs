#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn toboggan(entries: &Vec<String>, xplus: u16, yplus: u16) -> u16 {
    let mut x: u32 = 0;
    let mut y: u32 = 0;
    let mut trees = 0;
    let entries_len = entries.len() as u32;
    let gridwidth = entries[0].chars().count() as u32;
    while y < entries_len {
        x += xplus as u32;
        y += yplus as u32;
        x %= gridwidth;
        if y < entries_len && entries[y as usize].chars().nth(x as usize).unwrap() == '#' {
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

    println!("part1: {}", toboggan(&entries, 3, 1));

    let mut part2: u64 = 1;
    let slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]];
    for slope in &slopes {
        part2 *= toboggan(&entries, slope[0], slope[1]) as u64;
    }
    println!("part2: {}", part2);
}

#[bench]
fn bench_day03(b: &mut test::Bencher) {
    b.iter(|| main());
}
