#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore

N, A, B = sys.stdin.readline().rstrip().split()
P, Q, R, S = sys.stdin.readline().rstrip().split()

line1_min = max(1 - int(A), 1 - int(B))
line1_max = min(int(N) - int(A), int(N) - int(B))
line2_min = max(1 - int(A), int(B) - int(N))
line2_max = min(int(N) - int(A), int(B) - 1)


drawn_position = [(int(A), int(B))]
for i in range(line1_min, line1_max):
    pos = (int(A) + i, int(B) + i)
    drawn_position.append(pos)

for i in range(line2_min, line2_max):
    pos = (int(A) + i, int(B) - i)
    drawn_position.append(pos)
for i in range(int(P), int(Q) + 1):
    for j in reversed(range(int(R), int(S) + 1)):
        if (i, j) in drawn_position:
            print("#", end="")
        else:
            print(".", end="")
    print()
