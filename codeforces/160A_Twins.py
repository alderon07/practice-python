from sys import stdin

n = int(stdin.readline().strip())

coin_values = list(map(int, stdin.readline().strip().split()))


coin_values = sorted(coin_values, reverse=True)

my_sum = 0
# print(coin_values)

if len(coin_values) == 1:
    print(1)
elif len(coin_values) == 2 and coin_values[0] == coin_values[1]:
    print(2)
else:
    for i in range(0, len(coin_values)):
        postsum = sum(coin_values[i+1:]) 
        
        # print(f"sum={my_sum}")
        # print(f"postsum={postsum}")

        my_sum += coin_values[i] 
        if my_sum > postsum:
            break

    print(i+1)