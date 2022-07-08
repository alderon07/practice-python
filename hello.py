from functools import reduce
import numpy as np
from collections import defaultdict

my_dict = defaultdict(lambda: 0)

nums = [1,1,1,1,2,2,2,3,3,4,5,5,5]
a = 3
result = list()
for value in nums:
    my_dict[value] += 1


input = [1,2,3,4]
x = reduce(lambda x, y: x * y , input)
res = map(lambda e: x/e, input)

print("EHLO")
for i in range(len(nums) - 1, -1, -1):
    print(i)