#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn baggins(entries: &Vec<String>, name: String, types: &mut Vec<String>) {
    for bag in entries {
        let split = &bag.split(" ").collect::<Vec<&str>>();
        let bagname = format!("{} {}", split[0], split[1]);
        if split[4] != "no" {
            for foo in (4..split.len()).step_by(4) {
                let zbr = format!("{} {}", split[foo + 1], split[foo + 2]);
                if zbr == name {
                    if types.contains(&bagname.to_string()) == false {
                        types.push(bagname.to_string());
                    }
                    baggins(&entries, bagname.to_string(), types);
                }
            }
        }
    }
}

fn baggins2(entries: &Vec<String>, name: String, number: u32) -> u32 {
    let mut total = 0;
    for bag in entries {
        let split = &bag.split(" ").collect::<Vec<&str>>();
        let bagname = format!("{} {}", split[0], split[1]);
        if bagname == name {
            if split[4] != "no" {
                for foo in (4..split.len()).step_by(4) {
                    let subname = format!("{} {}", split[foo + 1], split[foo + 2]);
                    let subvalue = split[foo].parse::<u32>().unwrap();
                    total += number * baggins2(&entries, subname, subvalue);
                }
            }
        }
    }
    return total + number;
}

fn main() {
    let mut entries: Vec<String> = Vec::new();
    let f = File::open("../day07/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        entries.push(line.unwrap().to_string());
    }

    let mut types: Vec<String> = Vec::new();
    baggins(&entries, "shiny gold".to_string(), &mut types);
    println!("part1: {}", types.len());
    println!(
        "part2: {}",
        baggins2(&entries, "shiny gold".to_string(), 1) - 1
    );
}

#[bench]
fn bench_day07(b: &mut test::Bencher) {
    b.iter(|| main());
}
