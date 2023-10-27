from typing import List
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        onStack = [False for _ in arr]
        onStack[start] = True
        stack = [start]
        
        while (len(stack) > 0):
            indexToSearch = stack.pop()
            if(arr[indexToSearch] == 0):
                return True
            leftNewIndex = indexToSearch - arr[indexToSearch]
            rightNewIndex = indexToSearch + arr[indexToSearch]
            if(rightNewIndex <= len(arr) - 1 and not onStack[rightNewIndex]):
                stack.append(rightNewIndex)
                onStack[rightNewIndex] = True
            
            if(leftNewIndex >= 0 and not onStack[leftNewIndex]):
                stack.append(leftNewIndex)
                onStack[leftNewIndex] = True
        
        return False



sol = Solution()

print(sol.canReach([4,2,3,0,3,1,2], 5)) # true
print(sol.canReach([4,2,3,0,3,1,2], 0)) # true
print(sol.canReach([3,0,2,1,2], 2)) # false