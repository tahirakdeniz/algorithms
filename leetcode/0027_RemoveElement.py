from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for x in nums:
        if x != val:
            nums[i] = x
            i += 1
    return i

# case 1
nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))