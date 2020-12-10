#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;
use std::collections::HashMap;

fn main() {
    let mut adapters: Vec<i32> = Vec::new();
    let f = File::open("../day10/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        adapters.push(line.unwrap().parse::<i32>().unwrap());
    }

    // part 1
    let mut a = adapters.clone();
    a.push(0);
    a.sort();
    let mut one: i32 = 0;
    let mut three: i32 = 0;
    let adapters_total = a.len();
    for idx in 0..adapters_total {
        if idx < adapters_total - 1 {
            let val = a[idx + 1] - a[idx];
            if val == 1 {
                one += 1;
            } else {
                three += 1;
            }
        }
    }
    three += 1;
    println!("part1: {}", one * three);

    // part 2
    let mut b = adapters.clone();
    b.sort();
    let mut rep: HashMap<i32, i64> = HashMap::new();
    rep.insert(0, 1);
    for val in &b {
        for x in 0..4 {
            if !rep.contains_key(&(val - x)) {
                rep.insert(val - x, 0);
            }
        }

        let one = *rep.get(&(val - 1)).unwrap();
        let two = *rep.get(&(val - 2)).unwrap();
        let three = *rep.get(&(val - 3)).unwrap();
        let value = *rep.get(&(val)).unwrap();
        rep.insert(*val, value + one + two + three);
    }
    println!("part2: {}", rep[&b[b.len() - 1]]);
}

#[bench]
fn bench_day10(b: &mut test::Bencher) {
    b.iter(|| main());
}
