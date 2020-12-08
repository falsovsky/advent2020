use std::collections::HashMap;
use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn main() {
    let mut entries: Vec<Vec<String>> = Vec::new();
    let f = File::open("../day06/input").unwrap();
    let file = BufReader::new(&f);
    let mut tmp: Vec<String> = Vec::new();
    for line in file.lines() {
        let clean = line.unwrap().to_string();
        if clean == "" {
            entries.push(tmp);
            tmp = Vec::new()
        } else {
            tmp.push(clean);
        }
    }
    entries.push(tmp);

    let mut part1 = 0;
    let mut part2 = 0;
    for group in entries {
        let mut questions: HashMap<char, u16> = HashMap::new();
        for person in &group {
            for (_, c) in person.chars().enumerate() {
                let mut times: u16 = 0;
                if questions.contains_key(&c) {
                    times = *questions.get(&c).unwrap();
                }
                times += 1;
                questions.remove(&c);
                questions.insert(c, times);
            }
        }
        part1 += questions.len();
        for (_, value) in questions {
            if value == group.len() as u16 {
                part2 += 1;
            }
        }
    }
    println!("part1: {}", part1);
    println!("part2: {}", part2);
}
