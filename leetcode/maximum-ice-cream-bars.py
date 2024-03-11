class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        ans = 0
        for i in range(len(costs)):
            count += costs[i]
            if count <= coins:
                ans += 1
            else:
                count -= costs[i]
        return ans