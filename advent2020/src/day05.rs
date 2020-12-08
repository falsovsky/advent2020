use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

fn boarding(
    pass: String,
    pos: u32,
    mut rfirst: u32,
    mut rlast: u32,
    mut cfirst: u32,
    mut clast: u32,
) -> u32 {
    let mut changed = false;
    if pos < pass.len() as u32 {
        changed = true;
        let item = pass.chars().nth(pos as usize).unwrap();
        if item == 'F' {
            rlast = ((rlast as f64 / 2_f64) + (rfirst as f64 / 2_f64)).floor() as u32;
        } else if item == 'B' {
            rfirst = ((rlast as f64 / 2_f64) + (rfirst as f64 / 2_f64)).ceil() as u32;
        } else if item == 'L' {
            clast = ((clast as f64 / 2_f64) + (cfirst as f64 / 2_f64)).floor() as u32;
        } else if item == 'R' {
            cfirst = ((clast as f64 / 2_f64) + (cfirst as f64 / 2_f64)).ceil() as u32;
        }
    }
    if changed == true {
        return boarding(pass, pos + 1, rfirst, rlast, cfirst, clast);
    } else {
        return rlast * 8 + clast;
    }
}

fn main() {
    let mut part1 = 0;
    let mut entries: Vec<u32> = Vec::new();
    let f = File::open("../day05/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        let id = boarding(line.unwrap().trim().to_string(), 0, 0, 127, 0, 7);
        if id > part1 {
            part1 = id;
        }
        entries.push(id);
    }
    println!("part1: {}", part1);

    let mut part2 = 0;
    for i in (part1 as f64 / 2_f64) as u32..part1 {
        if entries.contains(&i) == false {
            part2 = i;
        }
    }
    println!("part2: {}", part2);
}
