from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1 for _ in ratings]

        for i in range(len(ratings) - 1):
            if(ratings[i + 1] > ratings[i]):
                candies[i + 1] = max(candies[i] + 1, candies[i + 1])
        
        for i in range(len(ratings) -1, 0, -1):
            if(ratings[i - 1] > ratings[i]):
                candies[i - 1] = max(candies[i] + 1, candies[i-1])

        return sum(candies)

sol = Solution()

print(sol.candy([1, 0, 2])) # 5
print(sol.candy([1, 2, 2])) # 4
print(sol.candy([1, 3, 2, 2, 1])) # 7