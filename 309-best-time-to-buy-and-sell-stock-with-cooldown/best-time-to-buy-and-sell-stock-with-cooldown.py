class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i, bought):
            if i >= len(prices):
                return 0

            if (i, bought) not in memo:
                if not bought:
                    memo[(i, bought)] = max(dp(i + 1, not bought) - prices[i], dp(i + 1, bought))
                else:
                    memo[(i, bought)] = max(dp(i + 1, bought), dp(i + 2, not bought) + prices[i])
            
            return memo[(i, bought)]
        
        return dp(0, False)

        