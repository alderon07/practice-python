from sys import stdin

a = stdin.readline().strip().split("+")
print("+".join(sorted(a)))