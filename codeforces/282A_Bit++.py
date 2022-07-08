from sys import stdin

line = stdin.readline()
num = 0
for line in stdin:
    x = line.strip()
    if x == "X++" or x == "++X":
        num += 1
    elif x == "--X" or x == "X--":
        num -= 1
    

print(num) 

