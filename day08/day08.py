#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read input
instructions = []
fp = open('input', 'r')
instructions = list(
    map(lambda s: [s[0], int(s[1])], [line.strip().split() for line in fp])
)
fp.close()

def run(code):
    pc = 0
    acc = 0
    size = len(code)
    visited = []
    while True:
        if pc in visited:
            return { 'error': 'infinite-loop', 'acc': acc }
        else:
            visited.append(pc)

        if pc >= size:
            return { "error": "exit", "acc": acc }

        opcode, args = code[pc]

        #print("PC={} ACC={} - {} {}".format(pc, acc, opcode, args))

        if opcode == "acc":
            acc += args

        if opcode == "jmp":
            pc += args
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
