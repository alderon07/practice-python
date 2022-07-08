from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    my_set = set()
    for e in nums:
        if e in my_set:
            print(e)
            return True
        my_set.add(e)
    return False