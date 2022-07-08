string = input()

res = 1
first = string[0]
for i in range(1, len(string)):
    if first == string[i]:
        res += 1
    else:
        res = 1
    
    # print(res)
    first = string[i]
    
    if res >= 7:
        break

if res < 7:
    print("NO")
else:
    print("YES")