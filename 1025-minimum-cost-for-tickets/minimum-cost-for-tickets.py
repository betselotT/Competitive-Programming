class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        def dp(i, covered):
            if i >= len(days):
                return 0
            if (i, covered) not in memo:
                if days[i] > covered:
                    one = dp(i + 1, days[i]) + costs[0]
                    seven = dp(i + 1, days[i] + 6) + costs[1]
                    thirty = dp(i + 1, days[i] + 29) + costs[2]
                    memo[(i, covered)] = min(one, seven, thirty)
                else:
                    memo[(i, covered)] = dp(i + 1, covered)

            return memo[(i, covered)]
        
        return dp(0, -1)