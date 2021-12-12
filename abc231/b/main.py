#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore

N = int(input())
S = []
for i in range(N):
    S.append(input())

counter = {}

for i in range(N):
    if S[i] not in counter:
            counter[S[i]] = 1
    else:
        counter[S[i]] += 1
print(max(counter,key=counter.get))
