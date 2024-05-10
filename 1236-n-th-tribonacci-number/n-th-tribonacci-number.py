class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict(int)
        def check(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            
            if n not in memo:
                memo[n] = check(n - 1) + check(n - 2) + check(n - 3)
            
            return memo[n]
        
        return check(n)