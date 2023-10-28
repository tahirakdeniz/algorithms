from typing import List, Dict, Set
from collections import deque
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        groups : Dict[int, Set[int]] = {}
        
        for i in range(len(arr)):
            if not arr[i] in groups:
                groups[arr[i]] = set()
            groups[arr[i]].add(i)
        
        distance = [float('inf') for _ in arr]
        distance[0] = 0

        queue = deque([0])
        
        while queue:
            i = queue.popleft()
            
            if(arr[i] in groups):
                s = groups.pop(arr[i])
                for j in s:                
                    if(distance[j] > distance[i] + 1):
                        queue.append(j)
                        distance[j] = distance[i] + 1
            
            
            
            newRightIndex = i + 1
            newLeftIndex = i - 1
            if(newRightIndex <= len(arr) - 1 and distance[newRightIndex] > distance[i] + 1 ):
                distance[newRightIndex] = distance[i] + 1
                queue.append(newRightIndex)

            if(newLeftIndex >= 0 and distance[newLeftIndex] > distance[i] + 1):
                distance[newLeftIndex] = distance[i] + 1
                queue.append(newLeftIndex)


        return distance[-1]

sol = Solution()

print(sol.minJumps([100,-23,-23,404,100,23,23,23,3,404])) # 3
print(sol.minJumps([7])) # 0
print(sol.minJumps([7,6,9,6,9,6,9,7])) # 1
print(sol.minJumps([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 11]))

