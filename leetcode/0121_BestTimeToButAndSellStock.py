from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = prices[-1] 
        maxProfit = 0
        
        for j in range(len(prices) - 2, -1, -1):
            maxProfit = max(max_value - prices[j], maxProfit)
            max_value = max(max_value, prices[j])

        return maxProfit

sol = Solution() 

print(sol.maxProfit([7,1,5,3,6,4])) # = 5
print(sol.maxProfit([7,6,4,3,1])) # = 0