#!/usr/bin/env python
# -*- coding: utf-8 -*-

groups = []

# read input
fp = open('input', 'r')
tmp = ""
for line in fp:
    if line.strip() == "":
        groups.append(tmp)
        tmp = ""
    else:
        tmp += line
fp.close()
groups.append(tmp)

# part 1
total = 0
for group in groups:
    answers = 0
    for question in range(97,123):
        if chr(question) in group:
            answers +=1
    total += answers
print('part1', total)
    
# part 2
total = 0
for group in groups:
    answers = {}
    persons = 0
    for person in group[:-1].split("\n"):
        for question in range(97,123):
            letter = chr(question)
            if chr(question) in person:
                if letter not in answers:
                    answers[letter] = 1
                else:
                    answers[letter] += 1
        persons += 1
    for answer in answers:
        if answers[answer] == persons:
            total +=1
print('part2', total)
