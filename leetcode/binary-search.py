from typing import List

def search(nums: List[int], target: int) -> int:
    l , r = 0, len(nums) - 1
    
    while l <= r:
        # don't take average because
        # mid will break for large ints
        # because of overflow
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return -1