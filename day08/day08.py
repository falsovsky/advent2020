#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

instructions = []

# read input
fp = open('input', 'r')
for line in fp:
    instructions.append(line.strip().split(" "))
fp.close()

def run(code):
    pc = 0
    acc = 0
    visited = []
    while True:
        if pc in visited:
            return {
                'error': 'infinite-loop',
                'acc': acc
            }
        else:
            visited.append(pc)

        try:
            opcode = code[pc][0]
            args = code[pc][1]
        except IndexError:
            return {
                "error": "exit",
                "acc": acc
            }

        #print(visited)
        #print("PC={} ACC={} - {} {}".format(pc, acc, opcode, args))

        if opcode == "acc":
            acc += int(args)

        if opcode == "jmp":
            pc += int(args)
        else:
            pc += 1

# part 1
print("part1 ", run(instructions)["acc"])

# part2
for i, v in enumerate(instructions):
    newcode = instructions.copy()
    if v[0] == "jmp":
        newcode[i] = ["nop", v[1]]
    elif v[0] == "nop":
        newcode[i] = ["jmp", v[1]]
    
    result = run(newcode)
    if result["error"] == "exit":
        print("part2 ", result["acc"])
        break


