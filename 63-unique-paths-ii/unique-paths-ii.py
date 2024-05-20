class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo = {}

        if obstacleGrid[0][0] == 1:
            return 0

        dp = [[0] * len(obstacleGrid[0]) for i in range(0, len(obstacleGrid))]
        def inbound(i, j):
            if 0 <= i < len(obstacleGrid) and 0 <= j < len(obstacleGrid[0]) and obstacleGrid[i][j] != 1:
                return dp[i][j]
            else:
                return 0
        
        if len(obstacleGrid) == 1 and obstacleGrid[0][0] == 1:
            return 0
        else:  
            dp[len(obstacleGrid) - 1][len(obstacleGrid[0]) - 1] = 1
        
        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[0]) - 1, -1, -1):
                if i == len(obstacleGrid) -1 and j == len(obstacleGrid[0]) - 1:
                    continue
               
                dp[i][j] = inbound(i + 1, j) + inbound(i, j + 1)
                
        return dp[0][0]