
from sys import stdin

def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

n, k = invr()
for x in range(k):
    if str(n)[-1] == "0":
        n //= 10;
    else:
        n -= 1

print(n)
