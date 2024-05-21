class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = []
        for i in range(len(triangle) - 1):
            dp.append([0] * len(triangle[i]))
        
        dp.append(triangle[-1])
        
        print(dp)
        summ = 0
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[i][j] = min(triangle[i][j] + dp[i + 1][j], triangle[i][j] + dp[i + 1][j + 1])
            
        return dp[0][0]