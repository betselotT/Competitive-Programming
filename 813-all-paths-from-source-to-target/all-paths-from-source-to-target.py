class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        stack = [(0, [0])]

        while stack:
            node, path = stack.pop()

            if node == len(graph) - 1:
                paths.append(path)

            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))

        return paths