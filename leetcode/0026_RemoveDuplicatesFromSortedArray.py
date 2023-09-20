from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    for x in nums:
        if x > nums[i]:
            i += 1
            nums[i] = x

    return i + 1
