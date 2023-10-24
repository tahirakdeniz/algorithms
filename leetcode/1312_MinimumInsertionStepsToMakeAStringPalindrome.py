class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1 for j in range(len(text2))] for _ in range(len(text1))]
        dp[0][0] = 1 if text1[0] == text2[0] else 0

        for j in range(1, len(text2)):
            dp[0][j] = 1 if text1[0] == text2[j] else dp[0][j-1]

        for i in range(1, len(text1)):
            dp[i][0] = 1 if text1[i] == text2[0] else dp[i-1][0]

        for i in range(1, len(text1)):
            for j in range(1, len(text2)):
                dp[i][j] =  dp[i-1][j-1] + 1 if text1[i] == text2[j] else max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)-1][len(text2)-1]
    
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestCommonSubsequence(s, s[::-1])
    
    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestPalindromeSubseq(s)



sol = Solution()

print(sol.minInsertions("zzazz")) # 0
print(sol.minInsertions("mbadm")) # 2
print(sol.minInsertions("leetcode")) # 5
print(sol.minInsertions("abcdef"))
print(sol.minInsertions("vsrgaxxpgfiqdnwvrlpddcz"))