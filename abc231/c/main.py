#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore


N, Q = map(int, input().split())

A = list(map(int, input().split()))


x = []
for i in range(Q):
    x.append(int(input()))
A.sort(reverse=True)
left = 0
right = N - 1
num = 0
for j in range(Q):
    while right - left > 0:
        print("left", left, "right", right)
        mid = int((left + right) / 2)
        if A[mid] < x[j]:
            right = mid + 1
        elif A[mid] > x[j]:
            left = mid - 1
        else:
            break
        num = mid
    print("mid", num)
