class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) not in memo:
                count = 0
                if i < m - 1:
                    count += dp(i + 1, j)
                if j < n - 1:
                    count += dp(i, j + 1)
                memo[(i, j)] = count

            return memo[(i, j)]
        
        return dp(0, 0)