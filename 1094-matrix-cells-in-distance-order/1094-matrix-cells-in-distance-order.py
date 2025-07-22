class Solution:
    def allCellsDistOrder(self, m: int, n: int, y: int, x: int) -> List[List[int]]:
        ans = []
        d = defaultdict(list)

        for i in range(m):
            for j in range(n):
                distance = abs(y - i) + abs(x - j)
                d[distance].append([i, j])

        for key in sorted(d):
            ans += d[key]

        return ans