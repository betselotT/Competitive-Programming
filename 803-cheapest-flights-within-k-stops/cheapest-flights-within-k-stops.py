class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))  
        
        prev = [float('inf')] * n
        prev[src] = 0

        for i in range(k + 1):
            curr = prev[:]
            for u in graph:
                for v, w in graph[u]:
                    curr[v] = min(curr[v], prev[u] + w)

            prev = curr[:]

        if prev[dst] != float('inf'):
            return prev[dst]
        else:
            return -1
