class Solution:
    def findChampion(self, n, edges):
        deg = [0] * n
        for edge in edges:
            deg[edge[1]] += 1
        ans = []
        for i in range(n):
            if deg[i] == 0:
                ans.append(i)
        if len(ans) > 1:
            return -1
        return ans[0]