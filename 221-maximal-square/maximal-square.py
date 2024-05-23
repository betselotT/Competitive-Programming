class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                matrix[i][j] = int(matrix[i][j])
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1])
        maxx = 0
        for i in range(row):
            m = max(matrix[i])
            maxx = max(maxx, m)
        
        return maxx * maxx