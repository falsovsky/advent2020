#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://stackoverflow.com/a/12174125
def set_bit(value, bit):
    return value | (1<<bit)

def clear_bit(value, bit):
    return value & ~(1<<bit)

def maskit(value, mask):
    v = value
    for idx in range(len(mask) - 1, -1, -1):
        bit = len(mask) - idx - 1
        if mask[idx] == "1":
            v = set_bit(v, bit)
        elif mask[idx] == "0":
            v = clear_bit(v, bit)
    return v

def get_addresses(addr, mask):
    addresses = []
    v = addr
    has_x = False
    for idx in range(len(mask) - 1, -1, -1):
        bit = len(mask) - idx - 1
        if mask[idx] == "1":
            v = set_bit(v, bit)
        elif mask[idx] == "X":
            has_x = True
    addresses.append(v)
    if has_x:
        for idx in range(len(mask) - 1, -1, -1):
            bit = len(mask) - idx - 1
            for a in addresses:
                if mask[idx] == "X":
                    c = clear_bit(a, bit)
                    s = set_bit(a, bit)
                    if c not in addresses:
                        addresses.append(c)
                    if s not in addresses:
                        addresses.append(s)
    else:
        addresses.append(v)
    return addresses

# part1
ram = {}
fp = open('input', 'r')
mask = ""
for line in fp:
    if "mask = " in line:
        mask = line[7:].strip()
    else:
        idx = line.index("]")
        addr = int(line[4:idx])
        value = int(line[idx + 4:])
        ram[addr] = maskit(value, mask)
fp.close()
part1 = 0
for idx in ram:
    part1 += ram[idx]
print("part1", part1)

# part2
ram = {}
fp = open('input', 'r')
mask = ""
for line in fp:
    if "mask = " in line:
        mask = line[7:].strip()
    else:
        idx = line.index("]")
        addr = int(line[4:idx])
        value = int(line[idx + 4:])
        addrs = get_addresses(addr, mask)
        for a in addrs:
            ram[a] = value
fp.close()
part2 = 0
for idx in ram:
    part2 += ram[idx]
print("part2", part2)
