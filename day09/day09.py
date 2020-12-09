#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read input
cipher = []

fp = open('input', 'r')
for line in fp:
    cipher.append(line.strip())
fp.close()

def xmas(preamble_size = 25):
    for idx in range(preamble_size, len(cipher)):
        calc = []
        for x in range(idx - preamble_size, idx):
            for y in range(x + 1, idx):
                calc.append(int(cipher[x]) + int(cipher[y]))
        if int(cipher[idx]) not in calc:
            return int(cipher[idx])

def xmas2(target):
    for idx1 in range(0, len(cipher)):
        numbers = []
        total = 0

        val1 = int(cipher[idx1])
        numbers.append(val1)
        total += val1

        for idx2 in range(idx1 + 1, len(cipher)):
            val2 = int(cipher[idx2])
            numbers.append(val2)
            total += val2

            if total == target:
                numbers.sort()
                return numbers[0] + numbers[len(numbers) - 1]

# part 1
part1 = xmas(25)
print("part1", part1)

part2 = xmas2(part1)
print("part2", part2)