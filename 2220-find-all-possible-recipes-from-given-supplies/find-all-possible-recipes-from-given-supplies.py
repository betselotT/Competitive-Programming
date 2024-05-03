class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        deg = [0] * len(recipes)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                adj[ingredients[i][j]].append(i)
                deg[i] += 1

        ans = []
        queue = deque()
        visited = set()
        for i in supplies:
            queue.append(i)
            visited.add(i)

        while queue:
            node = queue.popleft()
            
            for neighbour in adj[node]:
                deg[neighbour] -= 1
                if deg[neighbour] == 0:
                    ans.append(recipes[neighbour])
                    queue.append(recipes[neighbour])

        return ans