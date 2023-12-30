from typing import List
class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        
        minimumCosts = [[_ for _ in e] for e in grid]

        for i in range(len(grid) - 1):
            for j in range(len(grid[i])):
                src = grid[i][j]
                if i == 0:
                    minimumCosts[i][j] = src
                    
                for j2 in range(len(grid[i + 1])):
                    totalCost = minimumCosts[i][j] + moveCost[src][j2] + grid[i + 1][j2]
                    minimumCosts[i + 1][j2] = totalCost if j == 0 else min(totalCost, minimumCosts[i + 1][j2])

        return min(minimumCosts[len(grid) - 1])
    

solution = Solution()

print(solution.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])) # 17
print(solution.minPathCost([[5,1,2],[4,0,3]], [[12,10,15],[20,23,8],[21,7,1],[8,1,13],[9,10,25],[5,3,2]])) # 6


