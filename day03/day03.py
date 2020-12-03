#!/usr/bin/env python
# -*- coding: utf-8 -*-

grid = []

# read input
fp = open('input', 'r') 
for line in fp:
    grid.append(line.strip())
fp.close()

def foo(xplus, yplus):
    x = 0
    y = 0
    trees = 0
    gridwidth = len(grid[0])
    while y <= len(grid):
        x += xplus
        y += yplus
        gridx = x

        while gridx >= gridwidth:
            gridx = gridx - gridwidth 

        if y < len(grid):
            if grid[y][gridx] == "#":
                trees += 1
    return trees

# part1
print('part1', foo(3, 1))

# part2
bar = [[1,1], [3,1], [5,1], [7,1], [1,2]]
result = 0
for z in bar:
    if result == 0:
        result = foo(z[0], z[1])
    else:
        result *= foo(z[0], z[1])
print('part2', result)
