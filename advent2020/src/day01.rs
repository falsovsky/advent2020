use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

fn main() {
    let mut entries: Vec<u32> = Vec::new();

    let f = File::open("../day01/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        entries.push(line.unwrap().parse::<u32>().unwrap());
    }
    let mut part1 = false;
    'outer: for x in &entries {
        for y in &entries {
            if part1 == false && x + y == 2020 {
                println!("part1: {}", x * y);
                part1 = true;
            }
            for z in &entries {
                if part1 == true && x + y + z == 2020 {
                    println!("part2: {}", x * y * z);
                    break 'outer;
                }
            }
        }
    }
}