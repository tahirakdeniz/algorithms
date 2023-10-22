from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lastBought = 0
        if len(prices) <= 1:
            return 0
        if len(prices) <= 2:
            if(prices[-1] - prices[-2] > 0):
                lastBought = prices[-2]
                return prices[-1] - prices[-2]
            
            return 0
        
        maxProfits = [0]*len(prices)
        maxProfits[-1] = 0

        if(prices[-1] - prices[-2] > 0):
                lastBought = prices[-2]
                maxProfits[-2] = prices[-1] - prices[-2]
        else:
            maxProfits[-2] = 0
        
        
        for j in range(len(maxProfits) - 3, -1, -1):
            maxProfit1 = maxProfits[j + 1]
            maxProfit2 = maxProfits[j + 2] + prices[j + 1] - prices[j]
            maxProfit3 = maxProfits[j + 1] + lastBought - prices[j]

            if maxProfit1 >= maxProfit2 and maxProfit1 >= maxProfit3:
                maxProfits[j] = maxProfit1 
            elif maxProfit2 >= maxProfit1 and maxProfit2 >= maxProfit3:
                maxProfits[j] = maxProfit2
                lastBought = prices[j]
            else:
                maxProfits[j] = maxProfit3
                lastBought = prices[j]

        return maxProfits[0]

sol = Solution() 

print(sol.maxProfit([7,1,5,3,6,4])) # = 7
print(sol.maxProfit([1, 2, 3, 4, 5])) # = 4
print(sol.maxProfit([7,6,4,3,1])) # = 0