class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])

        def dfs(i, j):
            curr = board[i][j]
            if curr == "#" or curr == ".":
                return False
            
            board[i][j] = "#"

            for i_off, j_off in [(0,1), (1, 0), (0, -1), (-1, 0)]:
                new_i, new_j = i+i_off, j+j_off
                if 0 <= new_i < m and 0 <= new_j < n:
                    dfs(new_i, new_j)
            return True
        
        res = 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == "X":
                    if dfs(x, y):
                        res += 1
        return res                       