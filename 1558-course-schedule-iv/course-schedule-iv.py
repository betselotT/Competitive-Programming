class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        deg = [0] * numCourses
        check = defaultdict(set)

        for n1, n2 in prerequisites:
            deg[n2] += 1
            adj[n1].append(n2)

        queue = deque()
        for i in range(numCourses):
            if deg[i] == 0:
                queue.append(i)


        while queue:
            node = queue.popleft()
            for neigh in adj[node]:
                check[neigh].add(node)
                check[neigh].update(check[node])

                deg[neigh] -= 1
                if deg[neigh] == 0:
                    queue.append(neigh)

        ans = []
        for q in queries:
            if q[0] in check[q[1]]:
                ans.append(True)
            else:
                ans.append(False)

        return ans