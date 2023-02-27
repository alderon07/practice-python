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

my_input = inlt()

my_input = sorted(my_input)

h = my_input[-1]
a = h - my_input[0]
b = h - my_input[1]
c = h - my_input[2]

print(f"{a} {b} {c}")