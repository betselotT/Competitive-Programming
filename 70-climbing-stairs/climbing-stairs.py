class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        def new(n):
            if n == 1 or n == 2:
                return n
            
            if n not in memo:
                memo[n] = new(n - 1) + new(n - 2)
            
            return memo[n]

        return new(n)