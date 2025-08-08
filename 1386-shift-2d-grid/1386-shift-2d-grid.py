class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        
        n = len(grid)
        m = len(grid[0])
        total_elements = n * m
        
        # Reduce k to avoid unnecessary full rotations
        k = k % total_elements
        
        # Create a new grid for the result
        new_grid = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                # Calculate the new position
                new_index = (i * m + j + k) % total_elements
                new_i = new_index // m
                new_j = new_index % m
                new_grid[new_i][new_j] = grid[i][j]
        
        return new_grid