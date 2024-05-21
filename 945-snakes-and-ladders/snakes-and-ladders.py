class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        
        def pos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c
            return [r, c]
        
        queue = deque()
        queue.append([1, 0])
        visited = set()

        while queue:
            square, moves = queue.popleft()

            for i in range(1, 7):
                next = square + i
                r, c = pos(next)
                if board[r][c] != -1:
                    next = board[r][c] 
                if next == length * length:
                    return moves + 1
                if next not in visited:
                    visited.add(next)
                    queue.append([next, moves + 1])

        return -1