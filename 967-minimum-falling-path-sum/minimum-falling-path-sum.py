class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        ans = matrix[0][0]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix)):
                if i > 0:
                    minn = matrix[i - 1][j]
                    if j > 0:
                        minn = min(minn, matrix[i - 1][j - 1])
                    if j < len(matrix) - 1:
                        minn = min(minn, matrix[i - 1][j + 1])
                    
                    matrix[i][j] += minn
                
                if i == len(matrix) - 1:
                    if j == 0:
                        ans = matrix[i][j]
                    else:
                        ans = min(ans, matrix[i][j])
        
        return ans