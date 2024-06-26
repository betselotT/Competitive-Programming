class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        indegree = defaultdict(int)
        outdegree = defaultdict(int)

        for trusts, trusted in trust:
            indegree[trusted] += 1
            outdegree[trusts] += 1

        for node, in_degree in indegree.items():
            if in_degree == n - 1 and outdegree[node] == 0:
                return node

        return -1