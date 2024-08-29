class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.R = len(grid)
        self.C = len(grid[0])
        self.lookup = {}

        for x in range(self.R):
            for y in range(self.C):
                self.lookup[grid[x][y]] = (x, y)

    def adjacentSum(self, value: int) -> int:
        x, y = self.lookup[value]
        total = 0
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.R and 0 <= ny < self.C:
                total += self.grid[nx][ny]
        return total

    def diagonalSum(self, value: int) -> int:
        x, y = self.lookup[value]
        total = 0
        for dx, dy in [(-1, 1), (-1, -1), (1, -1), (1, 1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < self.R and 0 <= ny < self.C:
                total += self.grid[nx][ny]
        return total


# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)