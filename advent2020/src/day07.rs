#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::collections::HashMap;

fn baggins(entries: &Vec<Vec<String>>, name: String, cache: &mut HashMap<String, Vec<String>>) -> Vec<String> {
    let mut types: Vec<String> = Vec::new();
    for bag in entries {
        let bagname = &format!("{} {}", bag[0], bag[1]);
        if bag[4] != "no" {
            for foo in (4..bag.len()).step_by(4) {
                let zbr = format!("{} {}", bag[foo + 1], bag[foo + 2]);
                if zbr == name {
                    if types.contains(&bagname) == false {
                        types.push(bagname.to_string());
                    }
                    let values: Vec<String>;
                    if cache.contains_key(bagname) {
                        values = cache.get(&bagname.to_string()).unwrap().to_vec();
                    } else {
                        values = baggins(&entries, bagname.to_string(), cache);
                        cache.insert(bagname.to_string(), values.clone());
                    }
                    for i in values {
                        if types.contains(&i) == false {
                            types.push(i);
                        }
                    }
                }
            }
        }
    }
    return types;
}

fn baggins2(entries: &Vec<Vec<String>>, name: String, number: u32) -> u32 {
    let mut total = 0;
    for bag in entries {
        let bagname = format!("{} {}", bag[0], bag[1]);
        if bagname == name {
            if bag[4] != "no" {
                for foo in (4..bag.len()).step_by(4) {
                    let subname = format!("{} {}", bag[foo + 1], bag[foo + 2]);
                    let subvalue = bag[foo].parse::<u32>().unwrap();
                    total += number * baggins2(&entries, subname, subvalue);
                }
            }
        }
    }
    return total + number;
}

fn main() {
    let mut entries: Vec<Vec<String>> = Vec::new();
    let f = File::open("../day07/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        let mut tmp: Vec<String> = Vec::new();
        for i in line.unwrap().to_string().split(" ").collect::<Vec<_>>() {
            tmp.push(i.to_string());
        }
        entries.push(tmp);
    }

    let mut cache: HashMap<String, Vec<String>> = HashMap::new();
    let types = baggins(&entries, "shiny gold".to_string(), &mut cache);
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
