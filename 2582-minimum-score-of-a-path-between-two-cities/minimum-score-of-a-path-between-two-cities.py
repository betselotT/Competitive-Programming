class Solution(object):
    def minScore(self, n, roads):
        adj = defaultdict(list)
        for i, j, k in roads:
            adj[i].append((j, k))
            adj[j].append((i, k))
        
        def dfs(i, res):
            if i in visited:
                return
            visited.add(i)
            for neigh, dist in adj[i]:
                res[0] = min(res[0], dist)
                dfs(neigh, res)

        res = [float("inf")]
        visited = set()
        dfs(1, res)
        return res[0]
