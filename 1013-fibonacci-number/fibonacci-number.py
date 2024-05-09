class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def new(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            
            if n not in memo:
                memo[n] = new(n - 1) + new(n - 2)
            
            return memo[n]

        return new(n)