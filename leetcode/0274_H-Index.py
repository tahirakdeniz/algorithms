from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr = sorted(citations)

        j = 0
        for i in range(len(arr)-1, -1, -1):
            if(arr[i] >= j + 1):
                j += 1
            else :
                return j
        return j


sol = Solution()
print(sol.hIndex([3,0,6,1,5])) # 3
print(sol.hIndex([1,3,1])) # 1