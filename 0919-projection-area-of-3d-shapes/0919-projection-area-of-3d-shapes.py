class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        
        xy, xz = 0, 0
        for row in grid:
            #xy
            for elem in row:
                if elem != 0:
                    xy += 1
            #xz
            xz += max(row)
        #yz
        yz = 0
        for i in range(n):
            col = [grid[j][i] for j in range(n)]
            yz += max(col)
        
        return xy + xz + yz