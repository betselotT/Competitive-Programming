class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = defaultdict(int)
        def dp(i, bought):
            if i >= len(prices):
                return 0

            if bought:
                if (i, bought) not in memo:
                    memo[(i, bought)] = max(dp(i + 1, not bought) - prices[i] - fee, dp(i + 1, bought))
            else:
                if (i, bought) not in memo:
                    memo[(i, bought)] = max(dp(i + 1, not bought) + prices[i], dp(i + 1, bought))
            
            return memo[(i, bought)]
        
        return dp(0, True)

        