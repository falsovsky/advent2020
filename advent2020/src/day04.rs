use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;
use std::collections::HashMap;
use regex::Regex;

fn main() {
    let mut entries: Vec<String> = Vec::new();
    let f = File::open("../day04/input").unwrap();
    let file = BufReader::new(&f);
    let mut tmp: String = "".to_string();
    for line in file.lines() {
        let clean = line.unwrap().trim().to_string();
        if clean == "" {
            entries.push(tmp);
            tmp = "".to_string();
        } else {
            tmp += &format!(" {}",&clean).to_string();
        }
    }
    entries.push(tmp);

    let mut rules: HashMap::<&str, Regex> = HashMap::new();
    rules.insert("byr", Regex::new(r"byr:(19[2-8][0-9]|199[0-9]|200[0-2])( |$)").unwrap());
    rules.insert("iyr", Regex::new(r"iyr:(201[0-9]|2020)( |$)").unwrap());
    rules.insert("eyr", Regex::new(r"eyr:(202[0-9]|2030)( |$)").unwrap());
    rules.insert("hgt", Regex::new(r"hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)( |$)").unwrap());
    rules.insert("hcl", Regex::new(r"hcl:(\#[a-f|\d]{6})( |$)").unwrap());
    rules.insert("ecl", Regex::new(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$)").unwrap());
    rules.insert("pid", Regex::new(r"pid:(\d{9})( |$)").unwrap());

    let mut part1 = 0;
    let mut part2 = 0;
    for entry in entries {
        let mut fail1 = false;
        let mut fail2 = false;
        for (item, rule) in &rules {
            let key = format!("{}:", item);
            if entry.find(&key) == None {
                fail1 = true;
            }
            if rule.is_match(&entry) == false {
                fail2 = true;
            }
        }
        if fail1 == false {
            part1 += 1;
        }
        if fail2 == false {
            part2 += 1;
        }
    }
    println!("part1: {}", part1);
    println!("part2: {}", part2);
}