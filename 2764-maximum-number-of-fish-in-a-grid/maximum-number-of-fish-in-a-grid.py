class Solution(object):
    def findMaxFish(self, grid):
        def check(x, y):
            total = grid[x][y]
            grid[x][y] = 0

            for roww, coll in directions:
                newR, newC = roww + x, coll + y

                if 0 <= newR < row and 0 <= newC < col and grid[newR][newC] > 0:
                    total += check(newR, newC)
            
            return total
        
        row = len(grid)
        col = len(grid[0])
        ans = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] > 0:
                    ans = max(check(i, j), ans)
        
        return ans