#[macro_use]
extern crate lazy_static;
extern crate regex;

use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;
use regex::Regex;
use std::time::{Duration, Instant};

lazy_static! {
    static ref RE_NAME: Regex = Regex::new(r"([\w ]+) bags contain").unwrap();
    static ref RE_CONTENTS: Regex = Regex::new(r"(\d+) ([\w ]+) bags?").unwrap();
}

fn baggins(entries: &Vec<String>, name: String, types: &mut Vec<String>) {
    let start = Instant::now();
    for bag in entries {
        for bagname in RE_NAME.captures_iter(&bag) {
            for content in RE_CONTENTS.captures_iter(&bag) {
                if content[2] == name {
                    if types.contains(&bagname[1].to_string()) == false {
                        types.push(bagname[1].to_string());
                    }
                    baggins(&entries, bagname[1].to_string(), types);
                }
            }
        }
    }
    println!("{} {:?}", name, start.elapsed());
}

fn baggins2(entries : &Vec<String>, name: String, number: u32) -> u32 {
    let mut total = 0;
    for bag in entries {
        for bagname in RE_NAME.captures_iter(&bag) {
            if bagname[1] == name {
                for content in RE_CONTENTS.captures_iter(&bag) {
                    total += number * baggins2(
                        &entries, content[2].to_string(), content[1].parse::<u32>().unwrap()
                    );
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
    println!("part2: {}", baggins2(&entries, "shiny gold".to_string(), 1) - 1);

}