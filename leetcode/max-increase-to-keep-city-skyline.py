class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        colArr = []
        rowArr = []
        for i in range(row):
            maximum = -1
            for j in range(col):
                maximum = max(maximum, grid[i][j])
            rowArr.append(maximum)
        for i in range(col):
            maximum = -1
            for j in range(row):
                maximum = max(maximum, grid[j][i])
            colArr.append(maximum)
        count = 0
        for i in range(len(rowArr)):
            for j in range(len(rowArr)):
                minimum = min(colArr[j], rowArr[i])
                diff = minimum - grid[i][j]
                count += diff
        return count