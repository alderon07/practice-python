from sys import stdin

num_of_test_cases = stdin.readline()

inputs = list(map(int, stdin.readlines()))
# print(inputs)

def min_cost(my_list) -> int:
    length = len(my_list)
    divide_list_by  = length // 2
    min_cost = -1
    curr_cost = 0
    for i in range(length):
        window_idx = i + divide_list_by
        if window_idx < length: 
            first_list = set(my_list[i: window_idx])
            sec_list = set(set(my_list) - first_list)
            # print(f"firstlist: {first_list}")
            # print(f"sec_list: {sec_list}")
            curr_cost = abs(sum(first_list) - sum(sec_list))
            # print(f"curr_cost: {curr_cost}")
            if min_cost == -1:
                min_cost = curr_cost
            min_cost = min(curr_cost, min_cost) 
    return min_cost


for value in inputs:
    my_weights = [2**x for x in range(1, value + 1)]
    print(min_cost(my_weights))