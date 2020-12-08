use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

#[derive(Clone)]
struct Instruction {
    opcode: String,
    argument: i16,
}

fn run(code: &Vec<Instruction>) -> (String, i16) {
    let mut pc: i16 = 0;
    let mut acc: i16 = 0;
    let size: u16 = code.len() as u16;
    let mut visited: Vec<i16> = Vec::new();
    loop {
        if visited.contains(&pc) {
            return ("infinite-loop".to_string(), acc)
        } else {
            visited.push(pc);
        }

        if pc >= size as i16 {
            return ("exit".to_string(), acc)
        }

        let opcode = &code[pc as usize].opcode;
        let argument = code[pc as usize].argument;

        if opcode == "acc" {
            acc += argument;
        }

        if opcode == "jmp" {
            pc += argument;
        } else {
            pc += 1
        }
    }
}

fn main() {
    let mut entries: Vec<Instruction> = Vec::new();
    let f = File::open("../day08/input").unwrap();
    let file = BufReader::new(&f);
    for line in file.lines() {
        let tmp = line.as_ref().unwrap().split(" ").collect::<Vec<_>>();
        entries.push(
            Instruction {
                opcode: tmp[0].to_string(),
                argument: i16::from_str_radix(tmp[1].trim(), 10).unwrap()
            }
        );
    }
    println!("part1: {}", run(&entries).1);

    for (k, _) in entries.iter().enumerate() {
        let mut newcode = entries.clone();
        if newcode[k].opcode == "jmp" {
            newcode[k] = Instruction { opcode: "nop".to_string(), argument: newcode[k].argument };
        } else if newcode[k].opcode == "nop"  {
            newcode[k] = Instruction { opcode: "jmp".to_string(), argument: newcode[k].argument };
        }
        let result = run(&newcode);
        if result.0 == "exit" {
            println!("part2: {}", result.1);
            break;
        }
    }
}