class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if len(board) == 0 or len(board[0]) == 0:
            return board
        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])

        def check(row_, col_):
            temp = 0
            for i, j in directions:
                new_row = row_ + i
                new_col = col_ + j

                if inbound(new_row, new_col) and board[new_row][new_col] == 'M':
                    temp += 1
            return temp

        def dfs(row, col):
            visited.add((row, col))

            mines = check(row, col)

            if mines == 0:
                board[row][col] = 'B'
                for i, j in directions:
                    new_row = row + i
                    new_col = col + j
                    if inbound(new_row, new_col) and (new_row, new_col) not in visited and board[new_row][new_col] == 'E':
                        dfs(new_row, new_col)
            else:
                board[row][col] = str(mines)

        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
        elif board[x][y] == 'E':
            dfs(x, y)
        return board