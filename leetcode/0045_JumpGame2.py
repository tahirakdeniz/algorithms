from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        currentStepLastIndex = 0
        nextStepLastIndex = 0
        count = 0
        for index in range(len(nums)): # todo write
            if(index >= len(nums) - 1): # if index is last index, then return count. 
                return count
            
            nextStepLastIndex = max(nums[index] + index, nextStepLastIndex) # move last step index of next step

            if(nextStepLastIndex >= len(nums) - 1): # if last step is last index, then return count + 1. 
                return count + 1
            
            if(index == currentStepLastIndex):
                currentStepLastIndex = nextStepLastIndex # if index became last, then move it to the nextStepLastIndex
                count += 1
            
        return count
            
        


sol = Solution()

print(sol.jump([2,3,1,1,4])) # 2
print(sol.jump([2,3,0,1,4])) # 2
print(sol.jump([0]))
print(sol.jump([1, 1]))
print(sol.jump([1, 1, 1]))
print(sol.jump([1, 1, 1, 1]))