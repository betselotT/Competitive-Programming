class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        final = 0
        if n == 0:
            return first
        elif n == 1:
            return second
        for _ in range(2, n + 1):
            final = first + second
            first = second
            second = final
        return final