#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

database = []

# read input
fp = open('input', 'r')
tmp = ""
for line in fp:
    if line.strip() == "":
        database.append(tmp)
        tmp = ""
    else:
        tmp += line.replace("\n", " ")
fp.close()
database.append(tmp)

fields = {
    'byr': r'byr:(19[2-8][0-9]|199[0-9]|200[0-2])( |$)',
    'iyr': r'iyr:(201[0-9]|2020)( |$)',
    'eyr': r'eyr:(202[0-9]|2030)( |$)',
    'hgt': r'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)( |$)',
    'hcl': r'hcl:(\#[a-f|\d]{6})( |$)',
    'ecl': r'ecl:(amb|blu|brn|gry|grn|hzl|oth)( |$)',
    'pid': r'pid:(\d{9})( |$)'
}

# part 1
valid = 0
for passport in database:
    fail = False
    for field in fields:
        if passport.find(field + ':') == -1:
            fail = True
    if fail == False:
        valid += 1
print('part1', valid)

# part 2
valid = 0
for passport in database:
    fail = False
    for field in fields:
        m = re.search(fields[field], passport) 
        if m == None:
            fail = True
    if fail == False:
        valid += 1
print('part2', valid)

