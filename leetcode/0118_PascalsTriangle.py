from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = []

        result.append([1])

        for i in range(1, numRows):
            row = [1] + [result[i - 1][j - 1] + result[i-1][j] for j in range(1, i)] + [1]
            result.append(row)
        
        return result

if __name__ == "__main__":
    solution = Solution()
    assert solution.generate(1) == [[1]], solution.generate(1)
    assert solution.generate(2) == [[1],[1,1]], solution.generate(2)
    assert solution.generate(5) == [
        [1],
        [1,1],
        [1,2,1],
        [1,3,3,1],
        [1,4,6,4,1]
    ], solution.generate(5)
