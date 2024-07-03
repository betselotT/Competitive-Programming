class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        check = [(1,0),(0,1)]
        def inbound(row, col):
            return (0 <= row < len(dungeon) and 0 <= col < len(dungeon[0]))

        memo = [[-inf] * len(dungeon[0]) for _ in range(len(dungeon))]
        def dfs(i, j):
            if memo[i][j] != -inf:
                return memo[i][j]
            if i == len(dungeon) - 1 and j == len(dungeon[-1]) - 1:
                return dungeon[i][j] if dungeon[i][j] < 0 else 0
            for dxn in check:
                r, c = i + dxn[0], j + dxn[1]
                if inbound(r,c ):
                    returned = dfs(r, c) + dungeon[i][j]
                    if returned >= 0:
                        memo[i][j] = 0
                    else:
                        memo[i][j] = max(memo[i][j], returned)
            return memo[i][j]

        return abs(dfs(0,0)) + 1