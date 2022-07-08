from sys import stdin

f = stdin

n, k = f.readline().strip().split()

res = 0

scores = [int(x) for x in f.readline().strip().split()]

kth_contestent = scores[int(k) - 1]

for score in scores:
    if score >= kth_contestent and score > 0:
        res += 1

print(res)