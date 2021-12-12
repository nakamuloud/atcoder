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
A = InputLI()

A.sort(reverse=True)
counter = 0
flag = True
while flag:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = int(A[i] / 2)
        else:
            flag = False
            break
    counter += 1

print(counter-1)
