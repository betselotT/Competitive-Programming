class Solution:
    def isPrintable(self, board: List[List[int]]) -> bool:
        ROWS , COLS = len(board) , len(board[0])
        colors = set()
        
        for row in range(ROWS):
            for col in range(COLS):
                colors.add(board[row][col])
        
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for color in colors:
            r = [ROWS , -1]
            c = [COLS , -1]
            
            for row in range(ROWS):
                for col in range(COLS):
                    if board[row][col] == color:
                        r[0] = min(row , r[0])
                        r[1] = max(row , r[1])
                        c[0] = min(col , c[0])
                        c[1] = max(col , c[1])
            
            for row in range(r[0] , r[1] + 1):
                for col in range(c[0] , c[1] + 1):
                    if board[row][col] != color:
                        graph[board[row][col]].append(color)
                        indegree[color] += 1

        queue = deque()

        for color in colors:
            if indegree[color] == 0:
                queue.append(color)
        
        ans = 0

        while queue:
            color = queue.popleft()
            ans += 1

            for neighbor in graph[color]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return ans == len(colors)