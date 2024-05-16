class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for i in range(m):
            a = [0] * (n)
            dp.append(a)
        dp[m - 1][n - 1] = 1
        def ans(i, j):
            if 0 <= i < m and 0 <= j < n:
                return dp[i][j]
            return 0

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                dp[row][col] = ans(row + 1, col) + ans(row, col + 1)
        
        return ans(0, 0)