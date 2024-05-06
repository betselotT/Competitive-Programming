class Solution:
    def __init__(self):
        self.root = []
        self.rank = []

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            rootX, rootY = rootY, rootX

        self.root[rootY] = rootX
        self.rank[rootX] += self.rank[rootY]

        return True

    def removeStones(self, stones):
        n = len(stones)
        self.root = [i for i in range(n)]
        self.rank = [1] * n

        xs = {}
        ys = {}
        count = 0

        for i, (x, y) in enumerate(stones):
            if x in xs:
                count += self.union(i, xs[x])
            else:
                xs[x] = i
            if y in ys:
                count += self.union(i, ys[y])
            else:
                ys[y] = i

        return count
