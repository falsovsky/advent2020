use regex::Regex;
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
    let mut entries: Vec<Password> = Vec::new();
    let re = Regex::new(r"(\d+)-(\d+) (\w): (\w+)").unwrap();
    let f = File::open("../day02/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        let zbr = &line.unwrap();
        let cap = re.captures(zbr).unwrap();
        let entry: Password = Password {
            low: cap[1].parse::<u8>().unwrap(),
            high: cap[2].parse::<u8>().unwrap(),
            letter: cap[3].chars().nth(0).unwrap(),
            password: (&cap[4]).to_string(),
        };
        entries.push(entry);
    }

    let mut part1 = 0;
    let mut part2 = 0;
    for entry in &entries {
        if is_valid_part1(entry) {
            part1 += 1;
        }
        if is_valid_part2(entry) {
            part2 += 1;
        }
    }
    println!("part1: {}", part1);
    println!("part2: {}", part2);
}
