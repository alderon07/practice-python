from sys import stdin
import math

m, n = map(int, stdin.readline().strip().split())

print(math.floor((m * n) / 2))
