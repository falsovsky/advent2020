#![feature(test)]

extern crate test;

use std::fs::File;
use std::io::BufRead;
use std::io::BufReader;

static EMPTY: char = 'L';
static OCCUP: char = '#';
static FLOOR: char = '.';

static RULES: [[i8; 2]; 8] = [
    [-1, -1], [-1, 0], [-1, 1],
    [ 0, -1],          [ 0, 1],
    [ 1, -1], [ 1, 0], [ 1, 1],
];

fn shallow_find(items: &Vec<Vec<char>>, x: i8, y: i8, xplus: i8, yplus: i8, height: &i8, width: &i8) -> (bool, char) {
    let newx = x + xplus;
    let newy = y + yplus;
    if newx >= 0 && newx < *height && newy >= 0 && newy < *width {
        let value = items[newx as usize][newy as usize];
        if value == EMPTY || value == OCCUP {
            return (true, value);
        }
    }
    return (false, ' ');
}

fn solve1(items: &Vec<Vec<char>>, height: &i8, width: &i8) -> (bool, Vec<Vec<char>>) {
    let mut seats = items.clone();
    let mut changed = false;
    for x in 0..*height {
        for y in 0..*width {
            let value: char = items[x as usize][y as usize];
            if value != FLOOR {
                let mut neighbours: Vec<char> = Vec::new();
                for rule in RULES.iter() {
                    let neighbour = shallow_find(items, x, y, rule[0], rule[1], height, width);
                    if neighbour.0 == true {
                        neighbours.push(neighbour.1);
                    }
                }
                let mut total = 0;
                for neighbour in neighbours {
                    if neighbour == OCCUP {
                        total += 1;
                    }
                }
                if value == EMPTY && total == 0 {
                    seats[x as usize][y as usize] = OCCUP;
                    changed = true;
                }
                if value == OCCUP && total >= 4 {
                    seats[x as usize][y as usize] = EMPTY;
                    changed = true;
                }
            }
        }
    }
    return (changed, seats);
}

fn deep_find(items: &Vec<Vec<char>>, x: i8, y: i8, xplus: i8, yplus: i8, height: &i8, width: &i8) -> (bool, char) {
    let mut newx = x;
    let mut newy = y;
    loop {
        newx += xplus;
        newy += yplus;
        if newx < 0 || newx >= *height || newy < 0 || newy >= *width {
            break;
        }
        let value = items[newx as usize][newy as usize];
        if value == EMPTY || value == OCCUP {
            return (true, value);
        }
    }
    return (false, ' ');
}

fn solve2(items: &Vec<Vec<char>>, height: &i8, width: &i8) -> (bool, Vec<Vec<char>>) {
    let mut seats = items.clone();
    let mut changed = false;
    for x in 0..*height {
        for y in 0..*width {
            let value: char = items[x as usize][y as usize];
            if value != FLOOR {
                let mut neighbours: Vec<char> = Vec::new();
                for rule in RULES.iter() {
                    let neighbour = deep_find(items, x, y, rule[0], rule[1], height, width);
                    if neighbour.0 == true {
                        neighbours.push(neighbour.1);
                    }
                }
                let mut total = 0;
                for neighbour in neighbours {
                    if neighbour == OCCUP {
                        total += 1;
                    }
                }
                if value == EMPTY && total == 0 {
                    seats[x as usize][y as usize] = OCCUP;
                    changed = true;
                }
                if value == OCCUP && total >= 5 {
                    seats[x as usize][y as usize] = EMPTY;
                    changed = true;
                }
            }
        }
    }
    return (changed, seats);
}

fn main() {
    let mut seats: Vec<Vec<char>> = Vec::new();
    let f = File::open("../day11/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        seats.push(line.unwrap().chars().collect());
    }
    let height: i8 = seats.len() as i8;
    let width: i8 = seats[0].len() as i8;

    let mut part1 = 0;
    let mut oldseats = seats.clone();
    'outer1: loop {
        let newseats = solve1(&oldseats, &height, &width);
        if newseats.0 == false {
            for l in newseats.1 {
                for c in l {
                    if c == OCCUP {
                        part1 += 1
                    }
                } 
            }
            break 'outer1;
        }
        oldseats = newseats.1.clone();
    }
    println!("part1: {}", part1);

    let mut part2 = 0;
    let mut oldseats = seats.clone();
    'outer2: loop {
        let newseats = solve2(&oldseats, &height, &width);
        if newseats.0 == false {
            for l in newseats.1 {
                for c in l {
                    if c == OCCUP {
                        part2 += 1
                    }
                } 
            }
            break 'outer2;
        }
        oldseats = newseats.1.clone();
    }
    println!("part2: {}", part2);
}

#[bench]
fn bench_day11(b: &mut test::Bencher) {
    b.iter(|| main());
}
