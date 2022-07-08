from sys import stdin

line_number = 1
x, y = -1, -1
for line in stdin:
    
    a = list(map(int, line.strip().split()))
    if 1 in a:
        x = line_number
        y = a.index(1) + 1
        break;
    line_number += 1

res = abs(3-x) + abs(3-y)
print(res)
