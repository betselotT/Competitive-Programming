class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo={}

        def dp(i, bought, count):
            if count >= 2:
                return 0
            if i >= len(prices):
                return 0
            if (i, bought, count) not in memo:
                if bought:
                    memo[(i, bought, count)] = max(-prices[i] + dp(i + 1, 0, count), dp(i + 1, 1, count))
                else:
                    memo[(i, bought, count)] = max(prices[i] + dp(i + 1, 1, count + 1), dp(i + 1, 0, count))
                    
            return memo[(i, bought, count)]
        
        return dp(0, 1, 0)
