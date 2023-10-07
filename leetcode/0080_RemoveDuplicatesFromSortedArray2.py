from typing import List
def removeDuplicates(nums: List[int]) -> int:
    r = 2
    for i in range(2, len(nums)):
        if nums[r - 1] == nums[r - 2] and nums[r - 1] == nums[i]:
            continue
        
        nums[r] = nums[i]
        r += 1
    return r + 1