class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)
        def dp(i, total):
            if total == 0:
                return 1
            if i >= len(coins):
                return 0
            if total < 0:
                return 0

            if (i, total) not in memo:
                take = dp(i, total - coins[i])
                not_take = dp(i + 1, total)
                memo[(i, total)] = take + not_take
                    
            return memo[(i, total)]
        
        return dp(0, amount)