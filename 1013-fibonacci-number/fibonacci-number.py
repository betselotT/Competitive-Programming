class Solution:
    def fib(self, n: int) -> int:
        first, second = 0, 1
        curr = 0
        for i in range(2, n + 1):
            curr = first + second 
            first = second
            second = curr
        
        if n == 0:
            return 0
        else:
            return second