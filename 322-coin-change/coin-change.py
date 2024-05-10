class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')  for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(len(dp)):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        
        if dp[-1] == float('inf'):
            return -1
        else:
            return dp[-1]