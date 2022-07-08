from sys import stdin

n, k = map(int, stdin.readline().split())
half_len = 0

if n % 2 == 0:
    half_len = n // 2
else:
    half_len = (n // 2) + 1

if k <= half_len:
    print(2*k - 1)
else:
    nth_even = abs(k - half_len)
    print(2*nth_even)