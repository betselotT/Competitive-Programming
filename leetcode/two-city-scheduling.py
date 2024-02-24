class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:-abs(x[0]-x[1]))
        countA, countB = 0, 0
        total = 0
        n= len(costs)
        for i in range(n):
            if costs[i][0] <= costs[i][1] and countA < n/2:
                total += costs[i][0]
                countA += 1
            elif costs[i][1] < costs[i][0] and countB < n/2:
                total += costs[i][1]
                countB += 1
            elif countB >= n/2:
                total += costs[i][0]
                countA += 1
            elif countA >= n/2:
                total += costs[i][1]
                countB += 1
        return total
        