from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        i = 0
        while i <= reachable and i < len(nums) - 1:
            reachable = max(i + nums[i], reachable)
            if(reachable >= len(nums) - 1):
                return True
            i += 1
                    
        return reachable == len(nums) - 1


sol = Solution()
print(sol.canJump([2,3,1,1,4])) # true
print(sol.canJump([3,2,1,0,4])) # false