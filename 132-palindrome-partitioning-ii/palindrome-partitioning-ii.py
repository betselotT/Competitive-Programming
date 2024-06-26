class Solution:
    def minCut(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        arr = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) + 1):
            dp[i] = len(s) - i
            
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i < 2 or arr[i + 1][j - 1]):
                    arr[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)

        return dp[0] - 1