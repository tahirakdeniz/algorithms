from typing import List

def majorityElement(nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return sorted(nums)[len(nums) // 2]

        count = {}
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        
        for num in count:
            if count[num] > len(nums) // 2:
                return num

if __name__ == "__main__":
    solution = Solution()
    assert solution.majorityElement([3,2,3]) == 3
    assert solution.majorityElement([2,2,1,1,1,2,2]) == 2
