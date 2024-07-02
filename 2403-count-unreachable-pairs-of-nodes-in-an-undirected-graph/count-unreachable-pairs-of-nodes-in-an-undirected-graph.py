class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = {i : i for i in range(n)}
        size = [0] * n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x]) 
            return parent[x]
        
        def union(x, y):
            parentX, parentY = find(x),  find(y)
            if parentX != parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]
        for x, y in edges:
            union(x, y)
        
        myDict = defaultdict(int)
        for i in range(n):
            parentt = find(i)
            myDict[parentt] += 1
        
        c = (n * (n-1)) // 2
        ans = c
        for val in myDict.values():
            ans -= (val * (val - 1)) // 2
        return ans