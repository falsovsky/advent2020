#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

# read input
adapters = []

fp = open('sample', 'r')
for line in fp:
    adapters.append(int(line.strip()))
fp.close()

# part 1
a = adapters[:]
a.append(0)
a.sort()
differences = []
adapters_total = len(a)
for idx in range(0, adapters_total):
    if idx < adapters_total - 1:
        differences.append(a[idx+1] - a[idx])
differences.append(3) # Diferença para o ultimo é sempre 3
print("part1", differences.count(1) * differences.count(3))


# part 2
b = adapters[:]
b.sort()
rep = {}
rep[0] = 1
for val in b:
    """
    Se o valor que vou alterar não existir adiciona-o a 0, para não dar KeyError. 
    O mesmo para (val - 1), (val - 2) e (val - 3)
    """
    for x in range(0, 4):
        if val - x not in rep:
            rep[val - x] = 0

    """
    So existem no maximo 3 numeros seguidos com 1 valor de distancia
    (0) - 1 - 4 - 5 - 6 - 7 - 10 - 11 - 12 - 15 - 16 - 19 - (22) | Resultado da parte 1 (sample)
        1   3   1   1   1   3    1    1    3    1    3    3      | Distancias entre cada valor
                ^^^^^^^^^

    # 0 = 1 (Adicionado manualmente porque não existem valores anteriores a 0)
    # 1 -> 1 (# 0) + 0 (#-1) + 0 (#-2) = 1
    # 4 -> 0 (# 3) + 0 (# 2) + 1 (# 1) = 1
    # 5 -> 1 (# 4) + 0 (# 3) + 0 (# 2) = 1
    # 6 -> 1 (# 5) + 1 (# 4) + 0 (# 3) = 2
    # 7 -> 2 (# 6) + 1 (# 5) + 1 (# 4) = 4
    #10 -> 0 (# 9) + 0 (# 8) + 4 (# 7) = 4
    #11 -> 4 (#10) + 0 (# 9) + 0 (# 8) = 4
    #12 -> 4 (#11) + 4 (#10) + 0 (# 9) = 8
    #15 -> 0 (#14) + 0 (#13) + 8 (#12) = 8
    #16 -> 8 (#15) + 0 (#14) + 0 (#13) = 8
    #19 -> 0 (#18) + 0 (#17) + 8 (#16) = 8

    Total de combinacoes = 8
    """

    um    = rep[val - 1]
    dois  = rep[val - 2]
    tres  = rep[val - 3]
    rep[val] += um + dois + tres

print("part2", rep[b[-1]])
