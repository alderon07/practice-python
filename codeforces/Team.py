from sys import stdin

f = stdin

num_of_lines = stdin.readline()

res = 0

for line in f:
    numbers = [int(x) for x in line.strip().split()]
    if sum(numbers) > 1:
        res += 1

print(res)