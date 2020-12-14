#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read input
nav = []
fp = open('sample', 'r')
for line in fp:
    nav.append(line.strip())
fp.close()

# part1
time = int(nav[0])
part1 = 0
distance = time
for bid in nav[1].split(','):
    if bid == 'x':
        continue
    busid = int(bid)
    pos = 0
    while pos <= time:
        pos += busid
    dist = pos - time
    if dist < distance:
        distance = dist
        part1 = busid
print("part1", part1 * distance)

# part2
buspos = []
time = 0
x = 0
for bid in nav[1].split(','):
    time += 1
    if bid != 'x':
        buspos.append([int(bid), x])
    x += 1

x = 0
while True:
    loop = False
    #print(x, x + time - 1, int(buspos[-1][0]), (x + time - 1) % int(buspos[-1][0]) )
    if (x + time - 1) % int(buspos[-1][0]) == 0:
        loop = True
        for bus in buspos:
            if loop and (x + bus[1]) % bus[0]:
                loop = False
    if loop:
        break

    x += buspos[0][0]

print('part2', x)
