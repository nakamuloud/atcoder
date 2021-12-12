#!/usr/bin/env python3
import sys
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right  # type: ignore
from collections import Counter, defaultdict, deque  # type: ignore
from fractions import gcd  # type: ignore
from heapq import heapify, heappop, heappush, heappushpop, heapreplace, merge  # type: ignore
from itertools import accumulate, combinations, permutations, product  # type: ignore


def InputLI():
    return list(map(int, sys.stdin.buffer.readline().split()))


def InputI():
    return int(sys.stdin.buffer.readline())


def InputLS():
    return sys.stdin.buffer.readline().rstrip().decode("utf-8").split()


def InputS():
    return sys.stdin.buffer.readline().rstrip().decode("utf-8")


def InputIR(n):
    return [InputI() for _ in range(n)]


def InputLIR(n):
    return [InputLI() for _ in range(n)]


def InputSR(n):
    return [InputS() for _ in range(n)]


def InputLSR(n):
    return [InputLS() for _ in range(n)]


def InputSRL(n):
    return [list(InputS()) for _ in range(n)]


def InputMSRL(n):
    return [[int(i) for i in list(InputS())] for _ in range(n)]


N = InputI()
a = InputLI()

a_max = max(a)
a_min = min(a)
a_max_i = a.index(a_max)
a_min_i = a.index(a_min)

if a_max + a_min >= 0:
    for i in range(N):
        a[i] += a_max

    for i in range(N - 1):
        if a[i] > a[i + 1]:
            a[i + 1] += a[i]
            print(i)
