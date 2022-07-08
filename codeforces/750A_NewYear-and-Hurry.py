from sys import stdin
from time import time

# 4 hours = 240 mins
TOTAL_TIME = 4 * 60 

n, k = map(int, stdin.readline().strip().split())

prev_sum, my_sum, res = 0, 0, 0
for i in range(1, n+1):
    time_per_problem_i = 5 * i
    my_sum += time_per_problem_i
    prev_sum = max(prev_sum, my_sum)
    if prev_sum <= TOTAL_TIME - k:
        res = i
print(res)