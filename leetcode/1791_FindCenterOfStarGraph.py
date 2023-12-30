from typing import List
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return set(edges[0]).intersection(edges[1]).pop()
    

solution = Solution()
print(solution.findCenter([[1,2],[2,3],[4,2]])) #2
print(solution.findCenter([[1,2],[5,1],[1,3],[1,4]])) #1